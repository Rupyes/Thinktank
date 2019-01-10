# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-09 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventphoto_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to=events.models.user_directory_path_vid)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_videos', to='events.Event')),
            ],
        ),
        migrations.AlterField(
            model_name='eventphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=events.models.user_directory_path_img),
        ),
    ]