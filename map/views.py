from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello TUTU')


def get_map(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'map/map.html', {'squirrels': squirrels})
