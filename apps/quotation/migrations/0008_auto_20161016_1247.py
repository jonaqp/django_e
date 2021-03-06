# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotation', '0007_quotationstore_code_qt_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationstore',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='quotationstore',
            name='exchange_rate',
        ),
        migrations.AddField(
            model_name='quotationstore',
            name='applicant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstore_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
