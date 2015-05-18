# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neenan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='trackfile',
        ),
        migrations.AddField(
            model_name='piece',
            name='composer',
            field=models.CharField(default='Nya', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='piece',
            name='conductor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='ensemble',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='key',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='movementname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='movementnumber',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='opus',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='piecetype',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='piece',
            name='soloist',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='composer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='track',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
