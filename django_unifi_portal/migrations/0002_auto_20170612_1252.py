# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_unifi_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unifiuser',
            options={'permissions': (('can_navigate', 'Can Navigate'),)},
        ),
    ]
