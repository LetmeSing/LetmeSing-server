# Generated by Django 4.2 on 2023-05-07 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_member_first_name_member_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='test2',
        ),
    ]
