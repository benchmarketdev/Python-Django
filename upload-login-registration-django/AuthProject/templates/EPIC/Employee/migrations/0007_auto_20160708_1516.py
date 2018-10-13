# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_auto_20160707_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeefamilydetails',
            name='aadharCopy',
            field=models.FileField(null=True, upload_to=b'static/private/employee/nominee/files/aadhar/%Y/%m/', blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='aadharNumber',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='bankAccount',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='bankName',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='bfPercentage',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='esicPercentage',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='gfPercentage',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='ifscCode',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='isBFNominee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='isDependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='isESICNominee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='isGFNominee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='isPFNominee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='pfPercentage',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/private/employee/nominee/files/photo/%Y/%m/', blank=True),
        ),
        migrations.AddField(
            model_name='employeefamilydetails',
            name='residenceCopy',
            field=models.FileField(null=True, upload_to=b'static/private/employee/nominee/files/residence/%Y/%m/', blank=True),
        ),
    ]
