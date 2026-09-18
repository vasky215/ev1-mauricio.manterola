from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido a App1</h1><p>Esta es la vista de inicio.</p>")

def acerca(request):
    return HttpResponse("<h1>Acerca de App1</h1><p>Esta app fue creada para la Evaluación Sumativa 1.</p>")