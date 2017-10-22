# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodo', '0009_auto_20171022_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 22, 6, 29, 40, 384364, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
