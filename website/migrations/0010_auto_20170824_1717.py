# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170824_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='short_title_el',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='short_title_en',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
