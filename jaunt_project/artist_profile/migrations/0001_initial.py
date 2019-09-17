# Generated by Django 2.1.7 on 2019-09-12 15:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('genre', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('contact_first_name', models.CharField(max_length=30)),
                ('contact_last_name', models.CharField(max_length=30)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('profile_pic', models.IntegerField(blank=True, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('bandcamp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]