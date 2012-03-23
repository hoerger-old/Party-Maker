# -*- coding: utf8 -*-
import datetime, random, sha
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.conf import settings

from main.forms import RegistrationForm
from main.models import UserProfile

def index(request):
    return render_to_response("index.xhtml",  context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+username).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()

            user_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            user_profile.save()
    
            email_subject = "PartyMaker EMail Bestätigung"
            email_text = "Hallo %s,\n du hast dich bei Party Maker regierstriert. Klicke auf den folgenden\
                Link um deinen Account zu aktivieren.\n http://localhost:8000/validate/%s\n mfG das PartyMaker Team" % (
                    username, activation_key)
            email_address=settings.REGISTRATION_EMAIL_ADDRESS
            send_mail(email_subject, email_text, email_address, [email])
            return HttpResponseRedirect('thanks')
    else: 
         form = RegistrationForm()
    return render_to_response('register.xhtml', {'form':form},  context_instance=RequestContext(request)) 

def thanks(request):
    return render_to_response('thanks.xhtml', context_instance=RequestContext(request)) 

def validate(request, activation_key):
    if request.user.is_authenticated():
        return render_to_response('validate.xhtml', {'has_account': True}, context_instance=RequestContext(request))
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('validate.xhtml', {'expired': True}, context_instance=RequestContext(request))
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('validate.xhtml', {'success': True}, context_instance=RequestContext(request))
