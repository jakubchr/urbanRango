# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-13 11:53
from __future__ import unicode_literals

from django.db import migrations
import xmlvalidator.fields.ContentTypeRestrictedFileField


class Migration(migrations.Migration):

    dependencies = [
        ('xmlvalidator', '0002_xmldocument_decree_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmldocument',
            name='xml',
            field=xmlvalidator.fields.ContentTypeRestrictedFileField.ContentTypeRestrictedFileField(upload_to='xmls'),
        ),
    ]
