# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0010_employeereferraldetails_referralname'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='department',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='designation',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employeemaster',
            name='location',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
