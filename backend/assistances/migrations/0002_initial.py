# Generated by Django 4.0 on 2022-03-31 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('assistances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aids', to='users.user', verbose_name='User'),
        ),
    ]
