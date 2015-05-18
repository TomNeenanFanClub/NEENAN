# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0006_auto_20150518_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='collection',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
