# Generated by Django 2.1.7 on 2019-10-15 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist_profile', '0006_auto_20191014_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistprofile',
            name='country',
        ),
    ]
