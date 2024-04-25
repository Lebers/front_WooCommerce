import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, get_object_or_404

#@login_required
def incio(request):
    return render(request, 'incio.html', {'api_url': settings.API_URL})

#def product(request):
#    return render(request, 'product.html', {'api_url': settings.API_URL})
def product(request, id=None):
    # Solo se pasa el ID al contexto si existe
    context = {'product_id': id} if id else {}
    return render(request, 'product.html', context)

def listProduct(request):
    return render(request, 'list_product.html', {'api_url': settings.API_URL})

def specialCatalogs(request, catalogoName=None):
    # Pasamos tanto la base URL de la API como el nombre del catálogo a la plantilla
    context = {
        'api_url': settings.API_URL,
        'catalogoName': catalogoName  # Asegúrate de que este parámetro se maneje adecuadamente si puede ser None
    }
    return render(request, 'special_catalogs.html', context)


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