from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('feedit.feeds.views',
    url(r'^$', 'home'),
    url(r'^feed/new$', 'new_feed'),
    url(r'^feed/(?P<feed_id>\d+)/$', 'feed'),
    url(r'^feed/(?P<feed_id>\d+)/add/$', 'add_feed'),
    url(r'^feed/(?P<feed_id>\d+)/refresh/$', 'refresh'),
    url(r'^entry/(?P<entry_id>\d+)/read/$', 'read'),
    url(r'^import/$', 'import_opml'),
)
