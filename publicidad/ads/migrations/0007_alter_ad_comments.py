# Generated by Django 3.2.4 on 2021-06-07 02:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0006_auto_20210607_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='comments',
            field=models.ManyToManyField(related_name='comments_owned', through='ads.Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
