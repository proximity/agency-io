# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150728_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
