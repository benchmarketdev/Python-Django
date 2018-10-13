# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Region', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('addedOn', models.DateTimeField(auto_now=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(related_name='StateAddedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('regionId', models.ForeignKey(blank=True, to='Region.Region', null=True)),
                ('updatedBy', models.ForeignKey(related_name='StateUpdatedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
