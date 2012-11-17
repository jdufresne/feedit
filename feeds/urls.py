from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('feedit.feeds.views',
    url(r'^$', 'home'),
    url(r'^feed/(?P<feed_id>\d+)/$', 'feed'),
    url(r'^feed/new/$', 'new_feed'),
    url(r'^feed/add/(?P<feed_id>\d+)/$', 'add_feed'),
    url(r'^refresh/(?P<feed_id>\d+)/$', 'refresh'),
    url(r'^import/$', 'import_opml'),
)
