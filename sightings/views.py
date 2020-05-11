from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello! Squirrels!')


def list_squirrel(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list.html', {'squirrels': squirrels})


def get_squirrel(request, unique_Squirrel_ID):
    squirrel = Squirrel.objects.all().filter(unique_Squirrel_ID=unique_Squirrel_ID)[0]
    return render(request, "sightings/sighting.html", {'squirrel': squirrel})


def get_map(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/map.html', {'squirrels': squirrels})


def stats(request):
    squirrels = Squirrel.objects.all()
    total = Squirrel.objects.all().count()
    am = len(squirrels.filter(shift='am'))
    pm = len(squirrels.filter(shift='pm'))
    shift_missing = total - am - pm
    adult = len(squirrels.filter(age='Adult'))
    juvenile = len(squirrels.filter(age='Juvenile'))
    age_missing = total - adult - juvenile
    percent_am = am / total * 100
    percent_pm = pm / total * 100
    percent_shift_missing = shift_missing / total * 100
    percent_adult = adult / total * 100
    percent_juvenile = juvenile / total * 100
    percent_age_missing = age_missing / total * 100

    return render(request, 'sightings/stats.html', {
        'Total': total,
        'AM': am,
        'Percent_am': percent_am,
        'PM': pm,
        'Percent_pm': percent_pm,
        'Shift_missing': shift_missing,
        'Percent_shift_missing':percent_shift_missing,
        'Adults': adult,
        'Percent_adult':percent_adult,
        'Juvenile': juvenile,
        'Percent_juvenile':percent_juvenile,
        'Age_missing': age_missing,
        'Percent_age_missing':percent_age_missing,

    })
