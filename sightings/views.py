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
    percent_am = round(am / total * 100, 2)
    percent_pm = round(pm / total * 100, 2)
    percent_shift_missing = round(shift_missing / total * 100, 2)
    percent_adult = round(adult / total * 100, 2)
    percent_juvenile = round(juvenile / total * 100, 2)
    percent_age_missing = round(age_missing / total * 100, 2)

    return render(request, 'sightings/stats.html', {
        'Total': total,
        'AM': am,
        'Percent_am': percent_am,
        'PM': pm,
        'Percent_pm': percent_pm,
        'Shift_missing': shift_missing,
        'Percent_shift_missing':percent_shift_missing,
        'Adult': adult,
        'Percent_adult': percent_adult,
        'Juvenile': juvenile,
        'Percent_juvenile': percent_juvenile,
        'Age_missing': age_missing,
        'Percent_age_missing': percent_age_missing,

    })
