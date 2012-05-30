from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

from dictionary.views import home, profile, add_item, add_entry, credits, items, entry, edit_entry, edit_item, alphabet, logout, public, login_error

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Social Auth urls.
    url(r'', include('social_auth.urls')),
    url(r'^login/$', redirect_to, {'url' : '/login/twitter'}),
    #url(r'^login_error/$', login_error, name='login_error'),
    url(r'^logout/$', logout, name='logout'),

    # Tweedictionary urls.
    url(r'^$', home, name='home'),
    url(r'^item/(?P<item_id>\d+)/', items, name='items'),
    url(r'^entry/(?P<entry_id>\d+)/', entry, name='entry'),
    url(r'^profile/', profile, name='profile'),
    url(r'^additem/', add_item, name='add_item'),
    url(r'^add_entry/(?P<item_id>\d+)/', add_entry, name='add_entry'),
    url(r'^credits/', credits, name='credits'),
    url(r'^edit_item/(?P<item_id>\d+)/', edit_item, name='edit_item'),
    url(r'^edit_entry/(?P<entry_id>\d+)/', edit_entry, name='edit_entry'),
    url(r'^alphabet/(?P<char>[A-Z]{1})/', alphabet, name='alphabet'),
    url(r'^public/(?P<user_id>\d+)/', public, name='public'),


)
