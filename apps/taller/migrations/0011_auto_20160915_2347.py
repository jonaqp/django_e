# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0010_vehicle_vin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status_vehicle',
            field=models.CharField(choices=[('TA1-1', 'Alquilado'), ('TA1-2', 'Mantenimient Income'), ('TA1-3', 'Disponible')], default='TA1-3', max_length=10),
        ),
    ]
