# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifs', '0003_auto_20160908_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='setcountdown',
            field=models.BooleanField(default=True),
        ),
    ]
