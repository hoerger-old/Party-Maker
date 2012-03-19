from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()

class UserFieldType(models.Model):
    name = models.CharField(max_length=20)

class UserField(models.Model):
    user = models.ForeignKey(User)
    field_type = models.ForeignKey(UserFieldType)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)

class Vote(models.Model):
    user = models.ForeignKey(User, related_name="vote_user") 
    voted_for = models.ForeignKey(User, related_name="vote_voted_for")
    rating = models.PositiveIntegerField()
                                
