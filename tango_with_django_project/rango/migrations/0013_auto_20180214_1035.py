# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-14 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_auto_20180214_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.RemoveField(
            model_name='page',
            name='user',
        ),
    ]
