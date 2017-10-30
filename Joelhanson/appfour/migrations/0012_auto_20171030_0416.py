# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0011_auto_20171028_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveldetails',
            name='details',
        ),
        migrations.AlterField(
            model_name='traveldetails',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
