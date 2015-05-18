# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0007_piece_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artpath',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]
