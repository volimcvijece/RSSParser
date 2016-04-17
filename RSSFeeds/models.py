from __future__ import unicode_literals

from django.db import models


class Feeds(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    is_active = models.BooleanField(default=False) #korisno

    def __str__(self):
        return self.title

#naslov, vrijeme objave, link, autor i link na sliku
class FeedItems(models.Model): 
    feed = models.ForeignKey(Feeds)
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    url = models.URLField(unique = True)
    author = models.CharField(max_length=200)
    img_url = models.URLField()

    class Meta:
        ordering = ["-timestamp"]
        #unique_together = ['title', 'url']

    def __unicode__(self):
        return self.title

    
    
    
