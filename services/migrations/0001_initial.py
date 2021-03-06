# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Server_URLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('servertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Server_Type')),
            ],
        ),
    ]
