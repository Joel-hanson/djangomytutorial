# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfour', '0010_auto_20171028_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traveldetails',
            old_name='author',
            new_name='username',
        ),
    ]
