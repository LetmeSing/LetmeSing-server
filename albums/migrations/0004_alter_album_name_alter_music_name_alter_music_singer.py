# Generated by Django 4.2 on 2023-05-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_options_alter_music_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='앨범 이름'),
        ),
        migrations.AlterField(
            model_name='music',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='음악 이름'),
        ),
        migrations.AlterField(
            model_name='music',
            name='singer',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='가수 이름'),
        ),
    ]
