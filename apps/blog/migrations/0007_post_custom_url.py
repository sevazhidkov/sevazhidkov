# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160229_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='custom_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
