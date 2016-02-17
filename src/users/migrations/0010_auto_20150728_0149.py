# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150715_2345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', null=True, verbose_name=b'Profile Pic'),
        ),
    ]
