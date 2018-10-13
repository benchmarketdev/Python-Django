# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_auto_20160708_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeefamilydetails',
            name='aadharCopy',
        ),
        migrations.RemoveField(
            model_name='employeefamilydetails',
            name='aadharNumber',
        ),
        migrations.RemoveField(
            model_name='employeefamilydetails',
            name='residenceCopy',
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='branchName',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='idCopy',
            field=models.FileField(null=True, upload_to=b'static/private/employee/nominee/files/id/%Y/%m/', blank=True),
        ),
        migrations.AlterField(
            model_name='employeefamilydetails',
            name='dateOfBirth',
            field=models.DateField(max_length=100, null=True, blank=True),
        ),
    ]
