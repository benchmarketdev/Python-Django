# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20160627_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemaster',
            old_name='sureName',
            new_name='surName',
        ),
    ]
