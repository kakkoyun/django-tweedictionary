from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

from dictionary.views import home, profile, additem, credits, items, edit, alphabet

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tweedictionary.views.home', name='home'),
    # url(r'^tweedictionary/', include('tweedictionary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Social Auth urls.
    url(r'', include('social_auth.urls')),
    url(r'^login/$', redirect_to, {'url' : '/login/twitter/'}),
    
    # Tweedictionary urls.
    url(r'^$', home, name='home'),
    url(r'^item/(?P<item_id>\d+)/', items, name='items'),
    #url(r'^profile/', profile, name='profile'),
    #url(r'^additem/', additem, name='additem'),
    url(r'^credits/', credits, name='credits'),
    #url(r'^edit/(?P<entry_id>\d+)/', edit, name='edit'),
    #url(r'^alphabet/(?[A-Z]{1})', alphabet, name='alphabet'),


)
