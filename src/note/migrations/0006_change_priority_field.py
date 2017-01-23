# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-15 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_note_priority_old_data_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='priority',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='priority_temp',
            new_name='priority',
        ),
    ]