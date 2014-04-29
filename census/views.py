from django.shortcuts import render

from .models import Citizen


def home(request):
    return render(request, 'census.html',
                  {'sum': Citizen.objects.count(),
                   'average_age': Citizen.objects.average_age()})
