# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160916_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitmeasurement',
            old_name='type_correlative',
            new_name='type_measurement',
        ),
    ]
