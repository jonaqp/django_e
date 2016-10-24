# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correlative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('type_correlative', models.CharField(choices=[('CRT-1', 'Factura'), ('CRT-2', 'Boleta'), ('CRT-3', 'Cotizacion'), ('CRT-4', 'Checklist')], max_length=10)),
                ('prefix', models.CharField(blank=True, max_length=20, null=True)),
                ('postfix', models.CharField(blank=True, max_length=20, null=True)),
                ('format', models.CharField(blank=True, max_length=20, null=True)),
                ('initial', models.IntegerField(default=1)),
                ('increment', models.IntegerField(default=1)),
                ('final', models.IntegerField(blank=True, null=True)),
                ('actual', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('reason_social', models.CharField(blank=True, max_length=100, null=True)),
                ('initial_exercise', models.DateTimeField(blank=True, null=True)),
                ('final_exercise', models.DateTimeField(blank=True, null=True)),
                ('nit', models.CharField(blank=True, max_length=20, null=True)),
                ('legal_representative', models.CharField(blank=True, max_length=100, null=True)),
                ('accountant', models.CharField(blank=True, max_length=100, null=True)),
                ('register_accountant', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('logo_url', models.ImageField(blank=True, null=True, upload_to='organization/')),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_subsidiary_organization', to='company.Organization')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='correlative',
            name='subsidiary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_correlative_subsidiary', to='company.Subsidiary'),
        ),
    ]