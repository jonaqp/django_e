# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20160910_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='document_type',
            field=models.CharField(blank=True, choices=[('', '--Choose--'), ('DOC-1', 'DNI'), ('DOC-2', 'RUC'), ('DOC-3', 'PASSPORT')], max_length=20, null=True),
        ),
    ]
