# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-15 13:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20180215_1752'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='kirrurl',
            managers=[
                ('custom_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]