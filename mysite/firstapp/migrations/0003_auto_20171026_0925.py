# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 09:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20171026_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 9, 25, 42, 413423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 9, 25, 42, 412980, tzinfo=utc)),
        ),
    ]
