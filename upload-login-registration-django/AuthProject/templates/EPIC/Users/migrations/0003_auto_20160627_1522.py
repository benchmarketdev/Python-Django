# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_usermanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='otpSent',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
