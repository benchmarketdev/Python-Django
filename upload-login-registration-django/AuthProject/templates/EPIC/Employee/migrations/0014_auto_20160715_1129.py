# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0013_auto_20160714_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeexperiencedetails',
            name='dateOfJoining',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeeexperiencedetails',
            name='dateOfRelieving',
            field=models.DateField(null=True, blank=True),
        ),
    ]
