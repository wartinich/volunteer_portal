# Generated by Django 4.1.2 on 2022-10-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='user photo'),
        ),
    ]