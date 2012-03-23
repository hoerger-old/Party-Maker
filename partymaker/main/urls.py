from django.conf.urls.defaults import *
import main.views

urlpatterns = patterns('', 
    (r'index.html$', main.views.index),
    (r'registration.html$', main.views.register),
    (r'thanks.html$', main.views.thanks),
    (r'validate/([0-9a-f]+)$', main.views.validate),
    (r'logout.html$',  'django.contrib.auth.views.logout', {"next_page": "index.xhtml"}),
    (r'login.html$', 'django.contrib.auth.views.login', {"template_name": "login.xhtml"}),
)
