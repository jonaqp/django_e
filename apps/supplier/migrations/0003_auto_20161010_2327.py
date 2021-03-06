# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20161010_2327'),
        ('supplier', '0002_auto_20161006_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierSubsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('subsidiary', models.ManyToManyField(related_name='supplier_suppliersubsidiary_subsidiary', to='company.Subsidiary')),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='subsidiary',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='document_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='document_type',
            field=models.CharField(choices=[('DOC-2', 'RUC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_supplierproduct_supplier', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='suppliersubsidiary',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_suppliersubsidiary_supplier', to='supplier.Supplier'),
        ),
        migrations.AlterUniqueTogether(
            name='suppliersubsidiary',
            unique_together=set([('supplier',)]),
        ),
    ]
