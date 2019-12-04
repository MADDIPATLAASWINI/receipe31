# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=20)),
                ('ingredients', models.CharField(max_length=20)),
                ('process', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='media/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
