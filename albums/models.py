from django.db import models
from accounts.models import Member


class Album(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    member = models.ForeignKey(Member, related_name="album",
                               on_delete=models.CASCADE, db_column="member", verbose_name="사용자 id값")
    name = models.CharField(max_length=20, null=True,
                            blank=True, verbose_name='앨범 이름')
    created_at = models.DateField(
        null=True, blank=True, verbose_name='앨범 생성일자')
    numOfSongs = models.IntegerField(
        null=True, blank=True, verbose_name='앨범 수록곡 수')
    description = models.CharField(
        null=True, blank=True, verbose_name="앨범 설명", max_length=50)


class Music(models.Model):
    music_id = models.AutoField(primary_key=True, null=False, blank=False)
    album = models.ForeignKey(
        Album, related_name='music', on_delete=models.CASCADE, db_column='album', verbose_name="앨범 id")
    name = models.CharField(max_length=20, null=True,
                            blank=True, verbose_name='음악 이름')
    singer = models.CharField(max_length=20, null=True,
                              blank=True, verbose_name='가수 이름')
