from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template import *
from .models import Feeds, FeedItems
from .forms import FeedsForm

import feedparser
import datetime
import json

def feeds_list(request):
    feeds = Feeds.objects.all()
    return render(request, "feeds_list.html",{"feeds":feeds})

def feeditems_list(request):
    feeditems = FeedItems.objects.all()
    #paginator
    paginator = Paginator(feeditems, 20)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    return render(request, "feeditems_list.html",{"feeditems":items})

#search
def feeditems_search(request):
    feedslist = FeedItems.objects.all()
    #igranje
    query = request.GET.get("feed_query")

    if query:
        
        feedslist=feedslist.filter(author__icontains = query)
    else:
        feedslist={}
        
    return render(request, "feeditems_search.html",{"feeds":feedslist})


#search - autocomplete
def get_names(request):
    data = request.GET
    query = data.get("term")
    if query:
        feeds = FeedItems.objects.filter(author__icontains = query)
    else:
        feeds = FeedItems.objects.all()
    results = []
    for feed in feeds:
        feed_json = {}
        feed_json['id'] = feed.id
        feed_json['label'] = feed.author
        feed_json['value'] = feed.author
        results.append(feed_json)
    data = json.dumps(results)
    #data = json.dumps(list(FeedItems.objects.filter(author__icontains=query).values('author')))
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def feeds_filt(request):
    #feeds = Feeds.objects.all()
    return render(request, "base2.html",{})

def feeds_filtered(request, id):
    #filtered = FeedItems.objects.filter(pk__in=id)
    filtered = get_list_or_404(FeedItems, feed=id)

    #paginator
    paginator = Paginator(filtered, 20)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    

    return render(request, "feeds_filtered.html",{"filtered":items})

def new_feed(request):
    if request.method=="POST":
        form = FeedsForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            duplicateFeed = Feeds.objects.filter(url = feed.url)
            if len(duplicateFeed)==0:
                #feedparser
                feedData = feedparser.parse(feed.url)         
                feed.title=feedData.feed.title            
                feed.save()

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
                    #TODO: datetime -> timezone
                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')
                    feedItems.timestamp = dateString
                    feedItems.save()
            return redirect('feeds_list')
    else:
        form = FeedsForm()
        
    form = FeedsForm()
    return render(request, 'new_feed.html', {"form":form})
