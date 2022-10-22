from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from assistance.constants import AssistanceStatus


class Category(models.Model):
    name = models.CharField(verbose_name="name", max_length=30)

    class Meta:
        db_table = "categories"
        verbose_name = "categories"
        verbose_name_plural = "category"
        ordering = ("-id",)

    def __str__(self):
        return self.name


class Assistance(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    description = models.TextField(
        verbose_name="description",
        max_length=2000
    )
    image = models.FileField(
        verbose_name="image",
        upload_to="assistance/",
        blank=True,
        null=True
    )
    payment_url = models.CharField(
        verbose_name="payment url",
        max_length=250
    )
    category = models.ForeignKey(
        Category,
        verbose_name="category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="category"
    )
    user = models.ForeignKey(
        "authentication.User",
        verbose_name="author",
        on_delete=models.CASCADE,
        related_name="user_assistance"
    )
    status = models.CharField(
        verbose_name="status",
        max_length=150,
        choices=[(v.name, v.value) for v in AssistanceStatus],
        default=AssistanceStatus.ASSISTANCE_IPS.value
    )
    created_at = models.DateTimeField(
        verbose_name="created",
        auto_now_add=True,
        auto_now=False
    )
    updated_at = models.DateField(
        verbose_name="updated",
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        db_table = "assistance"
        ordering = ("-id",)

    def str(self):
        return self.name


class AssistanceComment(MPTTModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(
        "authentication.User",
        verbose_name="author",
        on_delete=models.CASCADE,
        related_name="user_comments"
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    created_at = models.DateTimeField(
        verbose_name="created",
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        db_table = "assistance_comments"
        ordering = ("-id",)
