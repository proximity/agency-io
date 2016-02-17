# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150715_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='person',
            field=models.ForeignKey(to='users.Person'),
        ),
    ]
