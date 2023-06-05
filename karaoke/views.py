from django.shortcuts import render
from .models import Karaoke, Room
from .serializer import KaraokeSerializer, RoomSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class KaraokeViewSet(viewsets.ModelViewSet):
    queryset = Karaoke.objects.all()
    serializer_class = KaraokeSerializer
