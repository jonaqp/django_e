# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20161006_1124'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='unitmeasurement',
            unique_together=set([('type_measurement', 'name')]),
        ),
    ]