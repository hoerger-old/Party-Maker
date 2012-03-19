from django.conf.urls.defaults import *
import main.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^partymaker/', include('partymaker.foo.urls')),

    (r'^$', main.views.index),
    (r'^index.html$', main.views.index),
    (r'^registration.html$', main.views.register),
    (r'^thanks.html$', main.views.thanks),
    (r'^validate/([0-9a-f]+)$', main.views.validate),
    (r'^logout.html$',  main.views.user_logout),
    (r'^login.html$', 'django.contrib.auth.views.login', {"template_name": "login.xhtml"}),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/hanse/Projects/PartyMaker/partymaker/media'}),
)
