# Generated by Django 4.2 on 2023-05-16 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_created_at_album_description_album_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': '앨범', 'verbose_name_plural': '앨범'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': '음악', 'verbose_name_plural': '음악'},
        ),
    ]