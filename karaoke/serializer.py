from .models import Karaoke, Room
from rest_framework import serializers


class KaraokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karaoke
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
