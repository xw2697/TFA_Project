from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list_squirrel),
    path('<squirrel_id>/', views.get_squirrel),
]
