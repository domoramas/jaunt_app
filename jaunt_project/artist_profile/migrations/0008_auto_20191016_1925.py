# Generated by Django 2.1.7 on 2019-10-16 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist_profile', '0007_remove_artistprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
