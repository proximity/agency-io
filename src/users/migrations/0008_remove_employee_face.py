# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150715_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='face',
        ),
    ]
