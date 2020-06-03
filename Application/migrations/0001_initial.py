# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-21 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='primary_key=True')),
                ('name', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('students', models.IntegerField()),
                ('category', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='upload/')),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
