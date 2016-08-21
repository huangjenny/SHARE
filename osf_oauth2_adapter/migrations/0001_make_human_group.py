# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 17:29
from __future__ import unicode_literals

from django.db import migrations

from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig


def create_human_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name=OsfOauth2AdapterConfig.humans_group_name)


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_human_group),
    ]
