# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('totalEmp', models.IntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('pin', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=255, null=True, blank=True)),
                ('website', models.URLField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('createdOn', models.DateTimeField(auto_now=True, null=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
    ]
