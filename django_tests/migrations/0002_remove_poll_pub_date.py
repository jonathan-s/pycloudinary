# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='pub_date',
        ),
    ]