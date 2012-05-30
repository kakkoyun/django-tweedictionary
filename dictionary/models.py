from django.db import models
from django.contrib.auth.models import User
import datetime

class Item(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    creation_date = models.DateField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
	return self.name
    def save(self):
        self.name = self.name.lower()
        self.last_modified = datetime.datetime.now()
	super(Item, self).save()


class Entry(models.Model):
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, related_name="entries")
    date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    belong = models.ForeignKey(Item, related_name="entries")
    class Meta:
	ordering = ['-last_modified']
	verbose_name_plural = "Entries"
    def __unicode__(self):
        return self.content
    def save(self):
	self.last_modified = datetime.datetime.now()
	(self.belong).save()
	super(Entry, self).save()


