# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20170903_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='content',
            name='start_date',
        ),
        migrations.AddField(
            model_name='content',
            name='duration',
            field=models.IntegerField(blank=True, default=1995, null=True),
        ),
    ]
