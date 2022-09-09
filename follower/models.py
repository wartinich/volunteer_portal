from django.db import models

from authentication.models import User


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriber")

    class Meta:
        db_table = "followers"
