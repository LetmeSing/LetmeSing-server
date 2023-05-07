from django.db import models


class Karaoke(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=True,
                            blank=True, verbose_name='매장 명')
    remainingSeat = models.IntegerField(
        null=True, blank=True, verbose_name="잔여석")
    totalSeat = models.IntegerField(null=True, blank=True, verbose_name='총 좌석')
    callNumber = models.CharField(
        max_length=15, null=True, blank=True, verbose_name='매장 번호')
    address = models.CharField(
        max_length=40, null=True, blank=True, verbose_name='매장 주소')
    star = models.FloatField(null=True, blank=True, verbose_name='별점')
    waiting = models.IntegerField(
        null=True, blank=True, verbose_name="대기 팀 숫자")

    class Meta:
        verbose_name = '노래방'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id


class Room(models.Model):
    room_id = models.AutoField(primary_key=True, null=False, blank=False)
    karaoke = models.ForeignKey(Karaoke, related_name="room", on_delete=models.CASCADE,
                                db_column="id", verbose_name="노래방 id값")
    roomNum = models.CharField(
        blank=True, null=True, verbose_name='몇 번 방인지', max_length=5)
    capacity = models.IntegerField(blank=True, null=True, verbose_name="몇인실인지")
    remainSong = models.IntegerField(
        blank=True, null=True, verbose_name="남은 곡 수")
    remainTime = models.IntegerField(
        blank=True, null=True, verbose_name='잔여 시간(분)')
    status = models.IntegerField(
        blank=True, null=True, verbose_name='잔여 곡 3개 이하거나 잔여 시간 10분 이하이면 1')

    class Meta:
        verbose_name = "노래방 호실"
        verbose_name_plural = "노래방 호실들"

    def __int__(self):
        return self.room_id
