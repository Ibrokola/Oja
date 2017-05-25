# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='title',
            new_name='color',
        ),
        migrations.AddField(
            model_name='variation',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]