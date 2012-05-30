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
        
    def saveAs(self, request, entry):
	entry.content = self.cleaned_data["content"]
	entry.save()
        send(request, entry.id)
	return entry

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["owner", "last_modified", "creation_date"]

    def save(self, request):
        item = Item( name = self.cleaned_data["name"],
                owner = request.user)
        item.creation_date = datetime.datetime.now()
        item.save()
        return item

    def saveAs(self, request, item):
        item.name = self.cleaned_data["name"]
        item.save()
        return item
