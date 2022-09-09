from django.db import models

from authentication.models import User


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="owner")
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="subscriber")

    class Meta:
        db_table = "followers"
