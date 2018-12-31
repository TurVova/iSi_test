import jwt
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.serializers import jwt_payload_handler

from accounts.models import CustomUser


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        user_type = validated_data['user_type']
        user_obj = CustomUser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    username =  serializers.CharField()
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'token'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username:
            user = CustomUser.objects.filter(username=username)
            if user.exists():
                if user.get().check_password(password):
                    payload = jwt_payload_handler(user.get())
                    data['token'] = jwt.encode(payload, settings.SECRET_KEY)
                else:
                    raise ValidationError('Password incorrect, try again')
            else:
                raise ValidationError('A username is not valid')
        return data