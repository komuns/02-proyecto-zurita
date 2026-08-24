from django.shortcuts import render
from django.http import HttpResponse

def v1_inicio(request):
    return HttpResponse("Hola mundo, esta es la vista de inicio de mi tienda.")

def v2_inicio(request):
    return HttpResponse("Hola mundo, esta es la vista de inicio de mi tienda, versión 2.")

# Create your views here.
