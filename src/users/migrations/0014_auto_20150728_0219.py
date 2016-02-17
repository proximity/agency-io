# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150728_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=users.utils.user_directory_path, null=True, verbose_name=b'Profile Pic', blank=True),
        ),
    ]
