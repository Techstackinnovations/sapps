# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sappsapp', '0006_auto_20180122_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='disc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resources',
            name='disc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
