from django.conf.urls.defaults import *
import profiles.views

urlpatterns = patterns('', 
    (r'votes$', votes.views.votes)
)
