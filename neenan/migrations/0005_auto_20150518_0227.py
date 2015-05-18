# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0004_auto_20150518_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
