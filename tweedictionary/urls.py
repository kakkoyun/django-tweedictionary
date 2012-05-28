from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

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
    url(r'^login/$', redirect_to, {'url' : '/login/twitter'}),
    
    # Tweedictionary urls.
    url(r'^$', 'tweedictionary.dictionary.views.index', name='home'),
    #url(r'^(?I<item_id>\d+)/', 'tweedictionary.dictionary.views.item', name='items'),
    url(r'^profile/', 'tweedictionary.dictionary.views.profile', name='profile'),
    url(r'^additem/', 'tweedictionary.dictionary.views.additem', name='additem'),
    url(r'^credits/', 'tweedictionary.dictionary.views.credits', name='credits'),
    #url(r'^edit/(?E<entry_id>\d+)/', 'tweedictionary.dictionary.views.edit', name='edit'),
    #url(r'^alphabet/(?[A-Z]{1})', 'tweedictionary.dictionary.views.alphabet', name='alphabet'),


)
