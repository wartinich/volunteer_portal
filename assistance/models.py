from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=30)

    class Meta:
        db_table = "categories"
        verbose_name = "categories"
        verbose_name_plural = "category"
        ordering = ("-id",)

    def str(self):
        return self.name


class Assistance(models.Model):
    STATUS = (
        (10, "Setup"),
        (20, "Pause"),
        (30, "In progress"),
        (40, "Completed"),
    )

    name = models.CharField(verbose_name='name', max_length=200)

    category = models.ForeignKey(
        Category,
        verbose_name='category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='category'
    )
    user = models.ForeignKey(
        'authentication.User',
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='user_assistance'
    )

    status = models.IntegerField(verbose_name='status', choices=STATUS)

    created_at = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        auto_now=False
    )
    updated_at = models.DateField(
        verbose_name='updated',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        db_table = "assistance"
        ordering = ("-id",)

    def str(self):
        return self.name


class AssistanceImage(models.Model):
    assistance = models.ForeignKey(
        Assistance,
        verbose_name='assistance',
        on_delete=models.CASCADE,
        related_name='assistance_images'
    )
    image = models.ImageField(verbose_name='image', upload_to='assistance/')

    class Meta:
        db_table = "assistance_images"
        ordering = ("-id",)


class AssistancePayment(models.Model):
    assistance = models.ForeignKey(
        Assistance,
        verbose_name='assistance',
        on_delete=models.CASCADE,
        related_name='assistance_payment'
    )
    name = models.CharField(verbose_name='name', max_length=20)
    payment_url = models.URLField(verbose_name='payment url', max_length=240)

    class Meta:
        db_table = "assistance_payment"
        ordering = ("-id",)


class AssistanceComment(MPTTModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(
        'authentication.User',
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    created_at = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        db_table = "assistance_comments"
        ordering = ("-id",)
