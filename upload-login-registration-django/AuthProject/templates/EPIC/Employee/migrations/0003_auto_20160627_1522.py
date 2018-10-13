# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20160627_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemaster',
            old_name='firstName',
            new_name='sureName',
        ),
        migrations.RemoveField(
            model_name='employeemaster',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='employeemaster',
            name='middleName',
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='givenName',
            field=models.CharField(db_index=True, max_length=200, null=True, blank=True),
        ),
    ]
