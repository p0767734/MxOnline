# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-21 15:00
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_auto_20180118_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9'),
        ),
    ]