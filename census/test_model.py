from django.test import TestCase

from .models import Citizen

import pytest


@pytest.mark.django_db
class TestCitizen(TestCase):
    def setUp(self):
        Citizen(name='Grace', age=66).save()
        Citizen(name='Guido', age=42).save()

    def test_sum(self):
        self.assertEquals(Citizen.objects.count(), 2)

    def test_median(self):
        self.assertEquals(Citizen.objects.median(), 54.0)
