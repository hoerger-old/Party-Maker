from django.db import models
from django.contrib.auth.models import User

class UserFieldType(models.Model):
    name = models.CharField(max_length=20)

class UserField(models.Model):
    user = models.ForeignKey(User)
    field_type = models.ForeignKey(UserFieldType)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
