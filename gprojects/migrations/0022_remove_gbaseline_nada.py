# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0021_gbaseline_nada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gbaseline',
            name='nada',
        ),
    ]
