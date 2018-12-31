from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from dialogs.models import Thread, Message
from dialogs.permissions import IsAdmin
from dialogs.serializers import (
    ThreadCreateSerializer,
    MessageCreateSerializer,
    UserThreadsListSerializer,
    MessageThreadsListSerializer,
    MessageSerializer
)


class ThreadCreateAPIView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateSerializer
    permission_classes = [IsAdmin, ]


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class UserThreadsListAPIView(ListAPIView):
    serializer_class = UserThreadsListSerializer

    def get_queryset(self):
        queryset = Thread.objects.filter(participants=self.request.user)
        return queryset


class MessageThreadRetrieveAPIView(RetrieveAPIView):
    queryset = Thread.objects.all()


    def get(self, request, *args, **kwargs):
        queryset = Message.objects.filter(thread=self.get_object())
        message_list = []
        for message in queryset:
            message_list.append(MessageThreadsListSerializer(message).data)
        serializer = MessageSerializer({'message_list': message_list})
        return Response(serializer.data)


class ThreadRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateSerializer
    permission_classes = [IsAdmin, ]

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = ThreadCreateSerializer(
            self.get_object(),
            data=serializer_data
        )
        if serializer.is_valid():
            serializer.save()
            if len(serializer.data['participants']) == 1:
                # delete Thread if there is only one admin
                self.get_object().delete()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
