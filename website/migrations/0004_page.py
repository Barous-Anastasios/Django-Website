# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170823_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=1500, null=True)),
                ('name', models.CharField(blank=True, max_length=1500)),
                ('friendlyurl', models.SlugField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True)),
                ('menu', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
    ]
