from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from dialogs.models import Thread
from dialogs.permissions import IsAdmin
from dialogs.serializers import ThreadCreateSerializer


class ThreadCreateCreateAPIView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateSerializer
    permission_classes = [IsAdmin, IsAuthenticated]