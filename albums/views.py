from django.shortcuts import render
from .models import Album, Music
from .serializer import AlbumSerializer, MusicSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
