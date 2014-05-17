from django.db import models

"""class Knight(models.Model):
    name = models.CharField(max_length=100)
    of_the_round_table = models.BooleanField()
    nametest = models.CharField(max_length=120)

class feed(models.Model):
    name = models.CharField(max_length=128, unique=True)
    genre = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    artist_flattr_account = models.URLField()

    def __unicode__(self):
        return self.name

class podcast(models.Model):
    #owner_feed = models.ForeignKey(feed)
    #name = models.CharField(default=feed.name)
    #genre = models.CharField(default=feed.genre)
    #artist = models.CharField(default=feed.artist)
    episode_number = models.IntegerField()
    #stream = models.FileField(upload_to='/uploads/')

    def __unicode__(self):
        return self.name
        """
