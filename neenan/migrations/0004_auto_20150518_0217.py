# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0003_auto_20150518_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
