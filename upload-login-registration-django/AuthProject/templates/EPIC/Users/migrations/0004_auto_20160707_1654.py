# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20160627_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='userType',
            field=models.CharField(default=b'U', max_length=2),
        ),
    ]
