# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_banner_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(default='', verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]
