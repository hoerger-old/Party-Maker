from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
                                
