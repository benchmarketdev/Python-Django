# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='addedBy',
            field=models.ForeignKey(related_name='EmployeeMasterAddedByUser', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='addedOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='status',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='steps',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='updatedOn',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
