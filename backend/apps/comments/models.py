from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from apps.assistances.models import Aid


class Comment(MPTTModel):
    aid = models.ForeignKey(Aid, on_delete=models.CASCADE, verbose_name='Aid', related_name='comment_aid')
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='User', related_name='comment_user')
    message = models.TextField(verbose_name='Message', max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.user
