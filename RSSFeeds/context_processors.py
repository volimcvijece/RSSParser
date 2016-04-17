from RSSFeeds.models import Feeds, FeedItems

def all_rss(request):
    return {'all_rss': Feeds.objects.all()}
