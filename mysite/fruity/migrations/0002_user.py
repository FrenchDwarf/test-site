# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('spin_count', models.IntegerField()),
                ('coin_count', models.IntegerField()),
                ('effect', models.CharField(max_length=10)),
            ],
        ),
    ]
