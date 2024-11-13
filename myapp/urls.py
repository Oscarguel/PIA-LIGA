from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.app),
    path('calendario/', views.calendario),
    path('campeonatos/', views.campeonatos),
    path('resultados/', views.resultados),
    path('Equipos/', views.equipos),



    path('', views.hello),
    
]
