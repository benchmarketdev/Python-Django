# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_auto_20160707_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='dateOfBirth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='dateOfJoining',
            field=models.DateField(null=True, blank=True),
        ),
    ]
