# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='check_in',
            new_name='is_checked_in',
        ),
    ]
