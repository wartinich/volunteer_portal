from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=180)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Aid(models.Model):
    title = models.CharField(verbose_name='Title', max_length=150)
    cover = models.ImageField(verbose_name='Image', upload_to='covers/', blank=True, null=True)
    description = models.TextField(verbose_name='Description', max_length=1000)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='User', related_name='aids')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='aid_category')
    payment_url = models.CharField(verbose_name='Payment URL', max_length=200)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'aids'

    def __str__(self):
        return self.title

    def comments_count(self):
        return self.comment_aid.count()

