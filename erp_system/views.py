import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

#@login_required
def incio(request):
    return render(request, 'incio.html', {'api_url': settings.API_URL})

def product(request):
    return render(request, 'product.html', {'api_url': settings.API_URL})


def newUser(request):
    return render(request, 'new_user_wherehouse.html', {'api_url': settings.API_URL})
def listUsers(request):
    return render(request, 'list_users.html', {'api_url': settings.API_URL})
def newWereHouse(request):
    return render(request, 'new_werehouse.html', {'api_url': settings.API_URL})
def listWere(request):
    return render(request, 'list_wherehouse.html', {'api_url': settings.API_URL})
def listProducts(request):
    return render(request, 'list_products.html', {'api_url': settings.API_URL})