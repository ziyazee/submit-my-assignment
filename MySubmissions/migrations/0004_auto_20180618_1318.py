# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MySubmissions', '0003_auto_20180618_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='uploadTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
