from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name',
                  'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}