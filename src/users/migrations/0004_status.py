# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_person_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_in', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
