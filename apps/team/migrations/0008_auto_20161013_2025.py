# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('team', '0007_auto_20161013_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_team_group', to='auth.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('group',)]),
        ),
    ]
