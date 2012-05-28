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
    url(r'^$', 'dictionary.views.index'),
    url(r'^(?P<item_id>\d+)/$', 'dictionary.views.item'),
    url(r'^profile/$', 'dictionary.views.profile'),
    url(r'^additem/$', 'dictionary.views.additem'),
    url(r'^credits/$', 'dictionary.views.credits'),
    url(r'^edit/(?P<entry_id>\d+)/$', 'dictionary.views.edit'),
    url(r'^alphabeth/(?[A-Z]{1})$', 'dictionary.views.alphabeth'),


)
