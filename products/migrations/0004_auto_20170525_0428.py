# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170525_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='color',
            field=models.CharField(default='Choose your option', max_length=120),
        ),
    ]