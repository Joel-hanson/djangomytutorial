# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0007_userprofileinfo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='traveldetails',
            name='paxname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
