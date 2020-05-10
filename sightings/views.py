from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello TUTU')


def list_squirrel(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list.html', {'squirrels': squirrels})


def get_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(unique_Squirrel_ID=squirrel_id)
    return HttpResponse(f'Hello! The following is the information of the request! <br>'
                        f'The latitude is {squirrel.latitude}. <br>'
                        f'The longitude is {squirrel.longitude}. <br>'
                        f'The unique_squirrel_Id is {squirrel.unique_Squirrel_ID}. <br>'
                        f'The shift is {squirrel.shift}. <br>'
                        f'The date is {squirrel.date}. <br>'
                        f'The age is {squirrel.age}.<br>')
