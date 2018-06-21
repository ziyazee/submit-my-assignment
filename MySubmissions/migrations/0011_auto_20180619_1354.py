# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MySubmissions', '0010_mysubjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MySubmissions.mysubjects'),
        ),
        migrations.AlterField(
            model_name='mysubjects',
            name='subjectName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
