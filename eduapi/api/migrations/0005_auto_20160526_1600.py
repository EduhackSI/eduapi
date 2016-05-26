# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160526_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='node',
        ),
        migrations.RemoveField(
            model_name='urlitem',
            name='item_ptr',
        ),
        migrations.AddField(
            model_name='node',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='UrlItem',
        ),
    ]