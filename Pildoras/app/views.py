from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("inicio")

def servicios(request):
    return HttpResponse("servicios")

def tienda(request):
    return HttpResponse("tienda")

def blog(request):
    return HttpResponse("blog")

def contacto(request):
    return HttpResponse("contact")