# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_auto_20170823_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='name',
        ),
        migrations.AddField(
            model_name='projeto',
            name='projeto',
            field=models.CharField(default='Nome do Projeto', max_length=50),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(default='Seu nome', max_length=50),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='sobre',
            field=models.CharField(default='Sobre', max_length=700),
        ),
    ]
