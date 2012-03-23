from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    user = models.ForeignKey(User, related_name="vote_user")
    voted_for = models.ForeignKey(User, related_name="vote_voted_for")
    rating = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
