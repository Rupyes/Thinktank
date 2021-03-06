# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-07 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190307_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='when_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='when_date',
            field=models.DateField(),
        ),
    ]
