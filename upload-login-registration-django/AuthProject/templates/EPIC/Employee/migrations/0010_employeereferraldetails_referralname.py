# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0009_auto_20160708_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeereferraldetails',
            name='referralName',
            field=models.CharField(db_index=True, max_length=100, null=True, blank=True),
        ),
    ]
