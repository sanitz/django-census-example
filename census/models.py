from __future__ import division
from django.db import models


class Citizen(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.age)
