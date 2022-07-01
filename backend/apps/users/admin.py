from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info',
         {
             'fields': ('user_photo', 'first_name', 'last_name', 'date_of_birth', 'telegram_username')
         }
         ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'password2'),
        }),
    )