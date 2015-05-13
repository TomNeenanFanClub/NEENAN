from django.db import models

# Create your models here.
# Generic track object
class Track(models.Model):
    track_id = models.IntegerField()
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    length = models.DurationField()
    play_count = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3,'3'), (4,'4'), (5, '5'), (0, 'no rating')))
    trackfile = models.FileField()
    artwork = models.ImageField()
    def __unicode__(self):  
        return self.name

# Non-classical song object
class Song(models.Model):
    track = models.ForeignKey(Track)
    album = models.CharField(max_length=100)
    song_no = models.IntegerField()
    artist = models.CharField(max_length=100)

# Classical piece object
class Classical(models.Model):
    composer = models.CharField(max_length=100)
    opus = models.IntegerField()
    movement = models.IntegerField()
    movement_name = models.CharField(max_length=100)
    performer = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100)
    performance_date = models.DateTimeField()
    category = models.CharField(max_length=100)
    
# Playlist object
#class Playlist(models.Model):
    # a multivalue filed i think

    
