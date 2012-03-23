from django.conf.urls.defaults import *
import profiles.views

urlpatterns = patterns('', 
    (r'(\w+)$', profiles.views.userprofile),
)
