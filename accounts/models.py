from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login_id, password, nickname, is_master):
        if not login_id:
            raise ValueError('Users must have a Login ID')
        if not nickname:
            raise ValueError('Users must have a nickname')

        user = self.model(
            login_id=login_id,
            nickname=nickname,
            is_master=is_master
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, login_id=None, password=None):
        superuser = self.create_user(
            login_id=login_id,
            password=password,
            nickname=nickname,
        )
        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class Member(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    login_id = models.CharField(
        max_length=30, unique=True, null=False, blank=False, verbose_name="로그인 ID")
    is_superuser = models.BooleanField(
        default=False, verbose_name="장고 슈퍼유저 여부")
    is_active = models.BooleanField(
        default=True, verbose_name="계정 활성화 여부")
    is_staff = models.BooleanField(
        default=False, verbose_name="관리자 페이지 접근 권한")
    is_master = models.IntegerField(default=0, verbose_name="점주 여부")
    nickname = models.CharField(
        unique=True, max_length=20, null=True, blank=True, verbose_name="닉네임")

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = verbose_name

        db_table = 'user'
