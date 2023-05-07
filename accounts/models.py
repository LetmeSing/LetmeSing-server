from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser 불러오기


class Member(AbstractUser):
    nickname = models.CharField(max_length=20, default="햇님달님")
