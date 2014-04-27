from django.shortcuts import render

from .models import Citizen


def home(request):
    return render(request, 'census.html',
                  {'sum': Citizen.objects.count(),
                   'median': Citizen.objects.median()})
