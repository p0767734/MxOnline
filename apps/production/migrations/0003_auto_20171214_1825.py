# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-14 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20171207_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='image',
            field=models.ImageField(max_length=1000, upload_to='productionimage/%Y/%m', verbose_name='\u4ea7\u54c1\u5c01\u9762\u56fe'),
        ),
    ]
