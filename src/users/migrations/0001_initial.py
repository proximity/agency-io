# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('agency', models.ForeignKey(to='users.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone_number', models.CharField(null=True, blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='users.Person')),
                ('department', models.ForeignKey(to='users.Department', null=True)),
            ],
            bases=('users.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='auth_user',
            field=models.OneToOneField(null=True, default=None, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
