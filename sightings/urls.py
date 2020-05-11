from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.get_map),
    path('sightings/', views.list_squirrel),
    path('sightings/<unique_Squirrel_ID>/', views.get_squirrel),
    path('sightings/stats', views.stats),
]
