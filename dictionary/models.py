from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    def __unicode__(self):
	return self.name

class Entry(models.Model):
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    belong = models.ForeignKey(Item)
    class Meta:
	verbose_name_plural = "Entries"
    def __unicode__(self):
        return self.content

