# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0014_auto_20160709_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='node_id',
            field=models.TextField(db_index=True),
        ),
    ]
