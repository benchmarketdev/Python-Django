# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0008_auto_20160708_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeereferencedetails',
            name='email',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeereferencedetails',
            name='knownFromDate',
            field=models.DateField(max_length=100, null=True, blank=True),
        ),
    ]
