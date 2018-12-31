from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from dialogs.models import Thread, Message


class ThreadCreateSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'id',
            'participants',
            'created',
            'updated'
        ]

    def validate(self, data):
        participants = data.get('participants')
        is_admin = 0
        for user in participants:
            if user.user_type == 'Admin':
                is_admin += 1
        if is_admin > 1 or is_admin < 1:
            raise ValidationError('User with Admin type should be one')
        return data


class MessageCreateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'sender',
            'thread',
        ]
        read_only_fields = [
            'sender'
        ]

    def create(self, validated_data):
        text = validated_data['text']
        thread = validated_data['thread']
        sender = validated_data['sender']
        message_obj = Message(text=text, thread=thread, sender=sender)
        message_obj.save()
        return validated_data


class UserThreadsListSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'id',
            'participants',
            'created',
            'updated',
        ]


class MessageThreadsListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'sender',
            'thread',
            'created',
        ]


class MessageSerializer(Serializer):
    message_list = serializers.ListField()
