# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 05:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0014_auto_20171030_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveldetails',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
