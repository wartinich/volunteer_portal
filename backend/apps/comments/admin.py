from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin):
    pass

