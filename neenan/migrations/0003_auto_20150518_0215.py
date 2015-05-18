# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0002_auto_20150518_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artpath',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
