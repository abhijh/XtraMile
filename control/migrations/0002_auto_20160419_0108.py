# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='alt_phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='how_know',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='organisation',
            field=models.CharField(max_length=100),
        ),
    ]
