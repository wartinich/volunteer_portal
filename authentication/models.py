from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models

from authentication.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=250, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=40)
    last_name = models.CharField(verbose_name='last name', max_length=80)
    birth_date = models.DateField(verbose_name='birth date')
    user_photo = models.ImageField(verbose_name='user photo', upload_to='users/')
    is_active = models.BooleanField(verbose_name='is active', default=True)
    is_superuser = models.BooleanField(verbose_name='is superuser', default=False)
    is_verified = models.BooleanField(verbose_name='is verified', default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f'{self.id}, {self.email}'

    class Meta:
        db_table = "users"
        ordering = ("-id",)

    @property
    def full_name(self):
        username = (
            self.first_name + " " + self.last_name
            if self.first_name and self.last_name else self.email
        )
        return username
