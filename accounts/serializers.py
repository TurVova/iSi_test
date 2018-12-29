from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = CustomUser(username=username)
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