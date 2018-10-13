# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0011_auto_20160709_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='band',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
