from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from dictionary.models import Entry, Item

#class UserAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(User,ItemAdmin)

# subclass AjaxSelectAdmin
class ItemAdmin(AjaxSelectAdmin):
    # create an ajax form class using the factory function
    #                     model,fieldlist,   [form superclass]
    form = make_ajax_form(Item, ({'name':'item'}))

admin.site.register(Item,ItemAdmin)
admin.site.register(Entry)
#admin.site.register(Item)

