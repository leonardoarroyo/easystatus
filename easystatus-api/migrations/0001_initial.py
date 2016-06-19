# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easystatus-api.Component')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='status_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easystatus-api.StatusPage'),
        ),
    ]
