from django.shortcuts import render
from .models import Album, Music
from .serializer import AlbumSerializer, MusicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class AlbumList(APIView):
    # album list를 보여줄 때
    def get(self, request):
        albums = Album.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    # 새로운 Album 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Album의 detail을 보여주는 역할
class AlbumDetail(APIView):
    # Album 객체 가져오기
    def get_object(self, pk):
        try:
            return Album.objects.get(id=pk)
        except Album.DoesNotExist:
            raise Http404

    # Album의 detail 보기
    def get(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    # Album 수정하기
    def put(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Album 삭제하기
    def delete(self, request, pk, format=None):
        album = self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Music의 List를 보여주는 역할
class MusicList(APIView):
    # Music list를 보여줄 때
    def get(self, request):
        musics = Music.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)

    # 새로운 Music 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Music의 detail을 보여주는 역할
class MusicDetail(APIView):
    # Music 객체 가져오기
    def get_object(self, pk):
        try:
            return Music.objects.get(music_id=pk)
        except Music.DoesNotExist:
            raise Http404

    # Music의 detail 보기
    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    # Music 수정하기
    def put(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Music 삭제하기
    def delete(self, request, pk, format=None):
        music = self.get_object(pk)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
