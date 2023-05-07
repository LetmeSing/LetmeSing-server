# Generated by Django 4.2 on 2023-05-07 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='앨범 생성일자'),
        ),
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='앨범 설명'),
        ),
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='앨범 이름'),
        ),
        migrations.AddField(
            model_name='album',
            name='numOfSongs',
            field=models.IntegerField(blank=True, null=True, verbose_name='앨범 수록곡 수'),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='음악 이름')),
                ('singer', models.CharField(blank=True, max_length=20, null=True, verbose_name='가수 이름')),
                ('album', models.ForeignKey(db_column='album', on_delete=django.db.models.deletion.CASCADE, related_name='music', to='albums.album', verbose_name='앨범 id')),
            ],
        ),
    ]