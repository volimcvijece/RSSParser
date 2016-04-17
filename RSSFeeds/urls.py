from django.conf.urls import url
from . import views


#specificnije (Duze) urlove navodimo prve!
urlpatterns = [
    url(r'^feeds/$', views.feeditems_list, name="feeditems_list"),
    url(r'^new$', views.new_feed, name="new_feed"),
    url(r'^$', views.feeds_list, name="feeds_list"),
    url(r'^get_names/$', views.get_names, name="get_names"),
    url(r'^search/$', views.feeditems_search, name="feeds_search"),
    url(r'^feed_filt/$', views.feeds_filt, name="feeds_filt"),
    url(r'^feed_filt/(?P<id>\d+)/$', views.feeds_filtered, name="feeds_filtered")
    

    ]

