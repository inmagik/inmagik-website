# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-30 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmz_blog', '0002_auto_20160930_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]