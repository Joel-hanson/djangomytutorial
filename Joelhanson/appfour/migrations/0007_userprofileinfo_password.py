# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0006_auto_20171028_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
