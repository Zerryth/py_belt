# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
