# Generated by Django 3.2.4 on 2021-06-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]
