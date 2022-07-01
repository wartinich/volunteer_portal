from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_photo = models.ImageField(verbose_name='User photo', upload_to='users/', blank=True, null=True)
    first_name = models.CharField(verbose_name='First name', max_length=30)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    phone_number = models.CharField(verbose_name='Phone number', max_length=13, unique=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True, null=True)
    telegram_username = models.CharField(verbose_name='Telegram username', max_length=35, blank=True, null=True)
    verified = models.BooleanField(verbose_name='Verified', default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'phone_number']
