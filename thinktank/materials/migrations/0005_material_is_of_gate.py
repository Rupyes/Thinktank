# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-28 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_auto_20190128_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='is_of_gate',
            field=models.BooleanField(default=False),
        ),
    ]
