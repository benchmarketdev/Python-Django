# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0004_auto_20160627_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='fatherName',
            field=models.CharField(db_index=True, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='motherName',
            field=models.CharField(db_index=True, max_length=200, null=True, blank=True),
        ),
    ]
