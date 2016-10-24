# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20161008_1358'),
        ('logistic', '0004_auto_20161020_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_condition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='logistic_purchaseorder_purchase_condition', to='core.PurchaseCondition'),
            preserve_default=False,
        ),
    ]