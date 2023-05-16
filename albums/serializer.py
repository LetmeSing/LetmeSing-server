from .models import Album, Music
from rest_framework import serializers


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    music = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = '__all__'
