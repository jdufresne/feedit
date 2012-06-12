from datetime import datetime
from time import mktime
import xml.etree.ElementTree
import feedparser
from django.shortcuts import get_object_or_404, redirect, render
from feedit.feeds.models import Feed, Entry
from feedit.feeds.forms import OpmlForm


def home(request):
    return render(request, 'feeds/home.html', {
        'feeds': Feed.objects.all(),
    })


def feed(request, feed_id):
    return render(request, 'feeds/feed.html', {
        'feed': get_object_or_404(Feed, pk=feed_id),
        'feeds': Feed.objects.all(),
    })


def refresh(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    if request.method == 'POST':
        feed_parsed = feedparser.parse(feed.uri)
        feed.title = feed_parsed.feed.title
        for entry_parsed in feed_parsed.entries:
            try:
                uuid = entry_parsed.id
            except AttributeError:
                # Some feeds don't set the ID properly, fallback to
                # the URI
                uuid = entry_parsed.link

            try:
                entry = Entry.objects.get(feed=feed, uuid=uuid)
            except Entry.DoesNotExist:
                entry = Entry(feed=feed, uuid=uuid)

            entry.link = entry_parsed.link
            entry.title = entry_parsed.title
            entry.author = entry_parsed.get('author')
            timestamp = mktime(entry_parsed.updated_parsed)
            entry.updated = datetime.fromtimestamp(timestamp)

            try:
                entry.content = entry_parsed.content[0].value
            except AttributeError:
                # If the there is no full content, get the summary
                entry.content = entry_parsed.summary

            entry.save()
    return redirect('feedit.feeds.views.feed', feed_id=feed_id)


def import_opml(request):
    if request.method == 'POST':
        form = OpmlForm(request.POST, request.FILES)
        if form.is_valid():
            root = xml.etree.ElementTree.parse(form.cleaned_data['file'])
            for tag in root.iterfind('//outline'):
                feed, created = Feed.objects.get_or_create(uri=tag.attrib['xmlUrl'])
                if created:
                    feed.title = tag.attrib['title']
                    feed.save()
            return redirect('feedit.feeds.views.home')
    else:
        form = OpmlForm()
    return render(request, 'feeds/import_opml.html', {
        'form': form,
    })
