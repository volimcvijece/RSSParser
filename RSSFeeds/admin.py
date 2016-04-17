from django.contrib import admin
from .models import Feeds, FeedItems

# Register your models here.

admin.site.register(Feeds)
admin.site.register(FeedItems)
