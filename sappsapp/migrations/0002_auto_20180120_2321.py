# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 17:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sappsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mcqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Mcqresults',
        ),
        migrations.DeleteModel(
            name='Psyctests',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='image',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profilechild',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profilechild',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profilechild',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profileparent',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profileparent',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profileparent',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profileteacher',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profileteacher',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profileteacher',
            name='location',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='attendance',
            name='day',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent')], default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='about',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='address',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='division',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='father',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='mother',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sappsapp.Profileteacher'),
        ),
        migrations.AddField(
            model_name='profilechild',
            name='univno',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='about',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='address',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profileparent',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sappsapp.Profileteacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='about',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='address',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='department',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='gender',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='idno',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profileteacher',
            name='qualification',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.CharField(choices=[(models.CharField(blank=True, max_length=200, null=True), 'c1'), (models.CharField(blank=True, max_length=200, null=True), 'c2'), (models.CharField(blank=True, max_length=200, null=True), 'c3'), (models.CharField(blank=True, max_length=200, null=True), 'c4')], default='c1', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='c1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='c2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='c3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='c4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='univresults',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='univresults',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='mcq',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sappsapp.Mcqs'),
        ),
    ]