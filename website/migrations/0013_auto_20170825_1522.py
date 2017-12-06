# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20170824_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='faculty_el',
            field=models.CharField(blank=True, choices=[('Head of Translog', 'Head of Translog'), ('Senior Research Fellows', 'Senior Research Fellows'), ('Research Fellows', 'Research Fellows'), ('Visiting Fellows', 'Visiting Fellows'), ('PhD Students', 'PhD Students')], max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='faculty_en',
            field=models.CharField(blank=True, choices=[('Head of Translog', 'Head of Translog'), ('Senior Research Fellows', 'Senior Research Fellows'), ('Research Fellows', 'Research Fellows'), ('Visiting Fellows', 'Visiting Fellows'), ('PhD Students', 'PhD Students')], max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(blank=True, choices=[('Research', 'Research'), ('Publications', 'Publications'), ('Academic', 'Academic'), ('News', 'News')], default='Research Areas', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('Areas', 'Areas'), ('Projects', 'Projects'), ('Conference Papers', 'Conference Papers'), ('Working Papers', 'Working Papers'), ('Journal Papers', 'Journal Papers'), ('Books', 'Books'), ('Courses', 'Courses'), ('Useful Links', 'Useful Links'), ('Software', 'Software'), ('Event', 'Event')], default='Research', max_length=1500, null=True),
        ),
    ]
