# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0012_employeemaster_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeidproof',
            name='voterCopy',
            field=models.FileField(null=True, upload_to=b'static/private/employee/files/dl/%Y/%m/', blank=True),
        ),
        migrations.AddField(
            model_name='employeeidproof',
            name='voterNumber',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
