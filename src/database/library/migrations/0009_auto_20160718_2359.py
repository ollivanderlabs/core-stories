# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-18 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20160301_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='locc_string',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='locc_with_P',
            field=models.BooleanField(default=False),
        ),
    ]
