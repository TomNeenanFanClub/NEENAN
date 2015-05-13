# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('artpath', models.CharField(max_length=100)),
                ('trackfile', models.FileField(upload_to='')),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('length', models.DurationField()),
                ('play_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('track_ptr', models.OneToOneField(serialize=False, to='neenan.Track', auto_created=True, parent_link=True, primary_key=True)),
                ('piecetype', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('opus', models.CharField(max_length=100)),
                ('movementname', models.CharField(max_length=100)),
                ('movementnumber', models.IntegerField()),
                ('soloist', models.CharField(max_length=100)),
                ('ensemble', models.CharField(max_length=100)),
                ('conductor', models.CharField(max_length=100)),
            ],
            bases=('neenan.track',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('track_ptr', models.OneToOneField(serialize=False, to='neenan.Track', auto_created=True, parent_link=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('track', models.IntegerField()),
                ('composer', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
            bases=('neenan.track',),
        ),
    ]
