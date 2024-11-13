
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def app(request):
    return render(request, "app.js")

def calendario(request):
    return render(request, "calendario.html")

def campeonatos(request):
    return render(request, "campeonatos.html")

def resultados(request):
    return render(request, "resultados.html")

def equipos(request):
    return render(request, "Equipos.html")

def hello(request):
    return HttpResponse("hello")



    