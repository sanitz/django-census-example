from __future__ import division
from django.db import models


class CitizenManager(models.Manager):
    def median(self):
        all_citizen = self.all()
        if not all_citizen:
            return 0
        return sum([citizen.age for citizen in all_citizen]) / len(all_citizen)


class Citizen(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    objects = CitizenManager()

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.age)
