# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 00:27
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

def create_share_robot_user(apps, schema_editor):
    ShareUser = apps.get_model('share', 'ShareUser')
    ShareUser.objects.create_robot_user(username=settings.APPLICATION_USERNAME, robot='')


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
        ('osf_oauth2_adapter', '0001_make_human_group')
    ]

    operations = [
        migrations.RunPython(create_share_robot_user),
    ]
