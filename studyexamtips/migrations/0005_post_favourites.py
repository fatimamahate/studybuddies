# Generated by Django 4.2.14 on 2024-07-25 20:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studyexamtips', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourites',
            field=models.ManyToManyField(related_name='user_favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]