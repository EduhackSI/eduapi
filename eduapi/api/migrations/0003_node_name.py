# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160526_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='name',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
    ]
