# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150728_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', null=True, verbose_name=b'Profile Pic', blank=True),
        ),
    ]
