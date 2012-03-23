from django.conf.urls.defaults import *
import main.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', main.views.index),
    (r'^index.html$', main.views.index),
    (r'^user/', include('partymaker.main.urls')),
    (r'^p/', include('partymaker.profiles.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/hanse/Projects/PartyMaker/partymaker/media'}),
)
