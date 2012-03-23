from django.conf.urls.defaults import *
import profiles.views

urlpatterns = patterns('', 
    (r'^$', main.views.index),
)
