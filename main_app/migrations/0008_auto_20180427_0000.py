# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-26 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_gift_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]