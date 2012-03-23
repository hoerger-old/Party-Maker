from django.conf.urls.defaults import *
import main.views

urlpatterns = patterns('', 
    (r'index$', main.views.index),
    (r'registration$', main.views.register),
    (r'thanks$', main.views.thanks),
    (r'validate/([0-9a-f]+)$', main.views.validate),
    (r'logout$',  'django.contrib.auth.views.logout', {"next_page": "/index"}),
    (r'login$', 'django.contrib.auth.views.login', {"template_name": "login.xhtml"}),
)
