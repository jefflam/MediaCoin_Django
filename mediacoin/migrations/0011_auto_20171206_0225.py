# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacoin', '0010_auto_20171206_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcode',
            name='code',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
