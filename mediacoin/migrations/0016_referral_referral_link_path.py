# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacoin', '0015_referral_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='referral_link_path',
            field=models.CharField(default='', max_length=10),
        ),
    ]
