from django.db import models

# Create your models here.
# Generic track object
class Track(models.Model):
    path = models.CharField(max_length=100)
    artpath = models.CharField(max_length=100)
    trackfile = models.FileField()
    date = models.DateTimeField()
    comment = models.TextField()
    length = models.DurationField()

    play_count = models.IntegerField()

# Non-classical song object
class Song(Track):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    track = models.IntegerField()
    composer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

# Classical piece object
class Piece(Track):
    piecetype = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    opus = models.CharField(max_length=100)
    movementname = models.CharField(max_length=100)
    movementnumber = models.IntegerField()
    soloist = models.CharField(max_length=100)
    ensemble = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100)

# Playlist object
#class Playlist(models.Model):
    # a multivalue filed i think


