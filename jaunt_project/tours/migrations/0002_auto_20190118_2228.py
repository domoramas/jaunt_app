# Generated by Django 2.1.5 on 2019-01-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_profile', '0010_auto_20190118_1850'),
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('region', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='TourProfile',
            new_name='Tour',
        ),
    ]
