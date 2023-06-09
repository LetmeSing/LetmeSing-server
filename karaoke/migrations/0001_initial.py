# Generated by Django 4.2 on 2023-05-24 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Karaoke',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='매장 명')),
                ('remainingSeat', models.IntegerField(blank=True, null=True, verbose_name='잔여석')),
                ('totalSeat', models.IntegerField(blank=True, null=True, verbose_name='총 좌석')),
                ('address', models.CharField(blank=True, max_length=40, null=True, verbose_name='매장 주소')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='위도')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='경도')),
                ('memberId', models.ForeignKey(db_column='memberId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='karaoke', to=settings.AUTH_USER_MODEL, verbose_name='유저 ID')),
            ],
            options={
                'verbose_name': '노래방',
                'verbose_name_plural': '노래방',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('roomNum', models.CharField(blank=True, max_length=5, null=True, verbose_name='몇 번 방인지')),
                ('capacity', models.IntegerField(blank=True, null=True, verbose_name='몇인실인지')),
                ('remainSong', models.IntegerField(blank=True, null=True, verbose_name='남은 곡 수')),
                ('remainTime', models.IntegerField(blank=True, null=True, verbose_name='잔여 시간(분)')),
                ('status', models.IntegerField(blank=True, null=True, verbose_name='잔여 곡 3개 이하거나 잔여 시간 10분 이하이면 1')),
                ('karaoke', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.CASCADE, related_name='room', to='karaoke.karaoke', verbose_name='노래방 id값')),
            ],
            options={
                'verbose_name': '노래방 호실',
                'verbose_name_plural': '노래방 호실들',
            },
        ),
    ]
