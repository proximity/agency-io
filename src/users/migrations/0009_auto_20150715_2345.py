# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_employee_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
