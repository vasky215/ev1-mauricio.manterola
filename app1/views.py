from django.shortcuts import render

def inicio(request):
    return render(request, 'app1/inicio.html')

def acerca(request):
    return render(request, 'app1/acerca.html')