import datetime
from django import forms
from dictionary.models import Entry, Item
from dictionary.operations import send

class EntryForm(forms.ModelForm):
    class Meta:
    	model = Entry
    	exclude = ["author", "date", "last_modified", "belong"]

    def save(self, request, item):
        entry = Entry(content = self.cleaned_data["content"],
        	      author = request.user,
                      belong = item)
        item.last_modified = datetime.datetime.now()
        item.save()
        entry.save()
        send(request, entry.id)
        return entry
