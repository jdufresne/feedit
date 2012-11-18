from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    uri = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def unread_by(self, user):
        return self.entries.exclude(pk__in=user.entry_set.all())

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title


class Entry(models.Model):
    feed = models.ForeignKey(Feed, related_name='entries')
    uuid = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField()
    content = models.TextField()
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['-updated']

    def __unicode__(self):
        return self.title
