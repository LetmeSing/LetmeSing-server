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
    review = models.TextField(null=True, blank=True, verbose_name="매장 후기")
    waiting = models.IntegerField(
        null=True, blank=True, verbose_name="대기 팀 숫자")

    class Meta:
        verbose_name = '노래방'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id
