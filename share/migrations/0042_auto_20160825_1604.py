# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0041_shareuser_is_trusted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardversion',
            name='award',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='award',
            old_name='award',
            new_name='name'
        ),
        migrations.RenameField(
            model_name='awardversion',
            old_name='award',
            new_name='name'
        ),
    ]
