from django.db import models
from django.contrib.auth.models import User

class UserFieldType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = "User Field Type"
        verbose_name_plural = "User Field Types"

class UserField(models.Model):
    user = models.ForeignKey(User)
    field_type = models.ForeignKey(UserFieldType)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    position = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = "User Field"
        verbose_name_plural = "User Fields"
