from django.db import models


class Petition(models.Model):
    title = models.CharField(verbose_name='title', max_length=200)
    petition_url = models.URLField(verbose_name='petition url', max_length=200)
    text = models.TextField(verbose_name='text')
    publish_date = models.DateTimeField(
        verbose_name='publish date',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        db_table = "petition"

    def __str__(self):
        return self.name
