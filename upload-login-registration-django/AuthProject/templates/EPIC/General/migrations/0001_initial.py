# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(null=True, blank=True)),
                ('addedOn', models.DateTimeField(auto_now=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(related_name='BandAddedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updatedBy', models.ForeignKey(related_name='BandUpdatedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(null=True, blank=True)),
                ('addedOn', models.DateTimeField(auto_now=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(related_name='DepartmentAddedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updatedBy', models.ForeignKey(related_name='DepartmentUpdatedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(null=True, blank=True)),
                ('addedOn', models.DateTimeField(auto_now=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(related_name='DesignationAddedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updatedBy', models.ForeignKey(related_name='DesignationUpdatedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(null=True, blank=True)),
                ('addedOn', models.DateTimeField(auto_now=True)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('addedBy', models.ForeignKey(related_name='RoleAddedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updatedBy', models.ForeignKey(related_name='RoleUpdatedBy', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
