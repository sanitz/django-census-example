from django.shortcuts import render

from . import Census
from .models import Citizen


def home(request):
    census = Census(Citizen.objects.all())
    return render(request, 'census.html',
                  {'sum': census.sum(),
                   'average_age': census.average_age()})
