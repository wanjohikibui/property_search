# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lr_number', models.CharField(max_length=100)),
                ('registered_to', models.CharField(max_length=256)),
                ('area', models.FloatField()),
                ('date_registered', models.DateTimeField()),
                ('registered_landuse', models.CharField(max_length=50)),
                ('brokers', models.BooleanField()),
                ('brokers_name', models.CharField(max_length=256, blank=True)),
                ('charged', models.BooleanField()),
                ('caveat', models.BooleanField()),
                ('loan', models.BooleanField()),
                ('courtorder', models.BooleanField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Parcel Data',
            },
        ),
        migrations.CreateModel(
            name='parcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectid', models.IntegerField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('lr_number', models.CharField(max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('app_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text=b'user@user.com', max_length=50)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('application_type', models.CharField(max_length=50, choices=[(b'Search', b'Search'), (b'Register', b'Register')])),
                ('county', models.CharField(max_length=50, choices=[(b'Nyeri', b'Nyeri'), (b'Kirinyaga', b'Kirinyaga'), (b'Kiambu', b'Kiambu'), (b'Laikipia', b'Laikipia')])),
                ('Area_Name', models.CharField(max_length=15, null=True)),
                ('closest_town', models.CharField(max_length=15, null=True)),
                ('description', models.TextField(max_length=256)),
                ('status', models.CharField(default=b'Unchecked', max_length=15, choices=[(b'Unchecked', b'Unchecked'), (b'Checked', b'Checked'), (b'Closed', b'Closed')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Applied Services',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 10, 31))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.AddField(
            model_name='data',
            name='objectid',
            field=models.OneToOneField(related_name='parcels', to='search.parcel'),
        ),
    ]
