from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('feedit.feeds.views',
    url(r'^$', 'home'),
    url(r'^feed/(?P<feed_id>\d+)/', 'feed'),
    url(r'^refresh/(?P<feed_id>\d+)/', 'refresh'),
    url(r'^import/$', 'import_opml'),
)
