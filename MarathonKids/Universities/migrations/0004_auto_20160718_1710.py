# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Universities', '0003_auto_20160718_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='kid_enrolled',
            new_name='kids_enrolled',
        ),
    ]
