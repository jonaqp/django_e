# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 00:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20161014_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_image',
            new_name='logo_profile',
        ),
    ]
