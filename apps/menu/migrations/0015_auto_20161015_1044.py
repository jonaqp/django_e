# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20161014_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammenuitem',
            name='permissions_menu',
        ),
        migrations.AddField(
            model_name='teammenu',
            name='permissions_menu',
            field=models.ManyToManyField(related_name='menu_teammenu_permissions_menu', to='menu.MenuPermissions'),
        ),
    ]
