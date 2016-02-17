# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_person_auth_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='emergency_contact_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='emergency_contact_phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='medical_alert',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
