# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sappsapp', '0004_auto_20180121_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sappsapp.Profilechild'),
        ),
    ]