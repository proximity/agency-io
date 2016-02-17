# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20150818_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='emergency_contact_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='emergency_contact_phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='medical_alert',
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emergency_contact_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emergency_contact_phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='medical_alert',
            field=models.TextField(null=True, blank=True),
        ),
    ]
