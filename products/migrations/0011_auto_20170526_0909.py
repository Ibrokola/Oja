# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productfeatured_make_image_carousel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeatured',
            old_name='acive',
            new_name='active',
        ),
    ]
