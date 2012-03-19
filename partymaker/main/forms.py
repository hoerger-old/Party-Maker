# -*- coding: utf8 -*- 
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30) 
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput,min_length=5)
    password2 = forms.CharField(widget=forms.PasswordInput,min_length=5)

    def clean_username(self):
        username= self.cleaned_data["username"]
        try: 
           User.objects.get(username=username) 
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('User "%s" existiert bereits!' % username)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Die Passwörter stimmen nicht überein!")
        return self.cleaned_data
