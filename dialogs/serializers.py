from rest_framework.serializers import ModelSerializer

from dialogs.models import Thread


class ThreadCreateSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'participants'
        ]