# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0015_auto_20171030_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveldetails',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appfour.UserProfileInfo'),
        ),
    ]
