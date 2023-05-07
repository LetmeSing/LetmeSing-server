# Generated by Django 4.2 on 2023-05-07 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0001_initial'),
    ]

    operations = [
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
