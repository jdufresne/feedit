import xml.etree.ElementTree
from django.shortcuts import redirect, render
from feedit.feeds.models import Feed
from feedit.feeds.forms import OpmlForm


def home(request):
    return render(request, 'feeds/home.html', {
        'feeds': Feed.objects.all(),
    })


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
            return redirect('feedit.feeds.views.import_opml')
    else:
        form = OpmlForm()
    return render(request, 'feeds/import_opml.html', {
        'form': form,
    })
