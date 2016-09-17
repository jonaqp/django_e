# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20160916_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitmeasurement',
            name='type_measurement',
            field=models.CharField(choices=[('UPM-1', 'PURCHASE LIQUID UNIT'), ('UPM-2', 'PURCHASE SOLID UNIT'), ('UPM-3', 'TRANSPORT UNIT'), ('UPM-4', 'DELIVERY UNIT'), ('UPM-5', 'STORAGE UNIT')], max_length=10),
        ),
    ]
