from django.core.management.base import BaseCommand
from RSSFeeds.models import Feeds, FeedItems
import feedparser
import datetime
from django.utils import timezone


class Command(BaseCommand):
    """
    Dohvati aktivne feedove
    """
    help = 'Update all feeds'

    def handle(self, *args, **options):
        
        for feed in Feeds.objects.all():            
            feedData = feedparser.parse(feed.url)         
            
            for entry in feedData.entries:
                feedItems = FeedItems()
                feedItems.feed = feed 
                feedItems.title = unicode(entry.title)
                feedItems.url = entry.link
                if 'media_thumbnail' in entry:
                    feedItems.img_url = entry['media_thumbnail'][0]['url']
                else:
                    pass
                feedItems.author = entry.author_detail.name
                d = datetime.datetime(*(entry.published_parsed[0:6]))
                #d = timezone.make_aware(d, timezone.get_current_timezone()) 
                dateString = d.strftime('%Y-%m-%d %H:%M:%S')
                
                feedItems.timestamp = dateString
                feedItems.save()


