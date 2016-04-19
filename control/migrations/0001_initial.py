# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('alt_phone', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('how_know', models.CharField(max_length=100, unique=True)),
                ('organisation', models.CharField(max_length=100, unique=True)),
                ('occupation', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]