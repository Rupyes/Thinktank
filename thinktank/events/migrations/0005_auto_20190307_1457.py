# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190307_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='when_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
