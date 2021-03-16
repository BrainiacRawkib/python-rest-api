# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-03-13 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gamecategory',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]