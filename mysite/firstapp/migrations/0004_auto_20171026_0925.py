# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 09:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20171026_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 9, 25, 58, 56349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 9, 25, 58, 55903, tzinfo=utc)),
        ),
    ]
