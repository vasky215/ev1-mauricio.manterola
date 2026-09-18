from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Bienvenido a App2</h1><p>Esta es la vista principal de App2.</p>")

def contacto(request):
    return HttpResponse("<h1>Contacto</h1><p>Esta es la vista de contacto de App2.</p>")