# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160912_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
