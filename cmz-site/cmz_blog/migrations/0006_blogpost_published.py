# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmz_blog', '0005_auto_20160930_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
