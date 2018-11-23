# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0012_auto_20181121_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='dep_code',
        ),
        migrations.RemoveField(
            model_name='employee_detail',
            name='emp_id',
        ),
        migrations.AddField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_detail',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]