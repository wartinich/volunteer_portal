from django.contrib import admin
from apps.assistances.models import Category, Aid


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Aid)
class AidAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category', 'created_at')
    list_display_links = ('id', 'title')
