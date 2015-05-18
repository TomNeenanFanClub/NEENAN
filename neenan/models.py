from django.db import models

# Create your models here.
# Generic track object
class Track(models.Model):
    path = models.CharField(max_length=200)
    artpath = models.CharField(max_length=200,blank=True)
    date = models.DateTimeField(blank=True,null=True)
    comment = models.TextField(blank=True)
    length = models.DurationField()

    play_count = models.IntegerField()

# Non-classical song object
class Song(Track):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    track = models.IntegerField()
    composer = models.CharField(max_length=100,blank=True)
    genre = models.CharField(max_length=100,blank=True)

# Classical piece object
class Piece(Track):
    piecetype = models.CharField(max_length=100,blank=True)
    collection = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True)
    composer = models.CharField(max_length=100)
    number = models.CharField(max_length=100,blank=True)
    key = models.CharField(max_length=100,blank=True)
    opus = models.CharField(max_length=100,blank=True)
    movementname = models.CharField(max_length=100,blank=True)
    movementnumber = models.IntegerField(blank=True,null=True)
    soloist = models.CharField(max_length=100,blank=True)
    ensemble = models.CharField(max_length=100,blank=True)
    conductor = models.CharField(max_length=100,blank=True)


    def _get_performer(self):
        string = ""
        if (self.soloist != ""):
            string += self.soloist

        if (self.conductor != ""):
            if (string != ""): string += ", "
            string += self.conductor

        if (self.ensemble != ""):
            if (string != ""): string += ": "
            string += self.ensemble

        return string

    performer = property(_get_performer)

    def __str__(self):
        lastname = self.composer.split(" ")[-1]
        string = lastname + ": "
        if (self.collection != ""):
            string += self.collection + " - "
            string += self.piecetype
        elif ((self.key == "" and str(self.number) == "") or self.piecetype == ""):
            string += self.name
        else:
            string += self.piecetype


        if (str(self.number) != ""):
            string += " No. "+str(self.number)

        if (self.key != ""):
            string += " in "+self.key

        if (self.opus != ""):
            string += ", "+self.opus

        if ((self.key != "" or str(self.number) != "") and self.name != "" and self.piecetype != ""):
            string += ', "' + self.name + '"'

        if (self.movementnumber != None and self.movementname != ""):
            string += " - " + toRoman (self.movementnumber) +". " + self.movementname

        if ( self.movementnumber == None and self.movementname != ""):
            string += " - " + self.movementname

        return string




##helper
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def toRoman(n):
    """convert integer to Roman numeral"""
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


# Playlist object
#class Playlist(models.Model):
    # a multivalue filed i think


