# Generated by Django 4.2 on 2023-05-24 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_is_admin_member_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '사용자'},
        ),
    ]