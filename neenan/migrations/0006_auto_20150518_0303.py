# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0005_auto_20150518_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='movementnumber',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
