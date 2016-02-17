# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20150802_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='auth_user',
        ),
    ]
