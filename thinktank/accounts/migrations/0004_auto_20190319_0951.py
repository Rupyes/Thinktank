# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_college_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.College'),
        ),
    ]
