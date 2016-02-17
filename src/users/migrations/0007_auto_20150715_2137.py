# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150715_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bio',
            field=models.TextField(default='poi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='face',
            field=models.ImageField(default='poi', upload_to=b'employees-faces/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(default='poi', max_length=255),
            preserve_default=False,
        ),
    ]
