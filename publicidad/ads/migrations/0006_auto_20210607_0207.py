# Generated by Django 3.2.4 on 2021-06-07 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0005_auto_20210607_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='comments',
            field=models.ManyToManyField(related_name='comments_comments', through='ads.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
