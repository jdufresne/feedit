from django.db import models


class Feed(models.Model):
    uri = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    #users = models.ManyToManyField('User')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def clean(self):
        if not self.title:
            self.title = self.uri
        super(Feed, self).clean()


class Entry(models.Model):
    feed = models.ForeignKey(Feed, related_name='entries')
    uuid = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField()
    content = models.TextField()

    class Meta:
        ordering = ['-updated']

    def __unicode__(self):
        return self.title
