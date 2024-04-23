import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from requests.auth import HTTPBasicAuth
from woocommerce import API

#@login_required
def incio(request):
    return render(request, 'incio.html', {'api_url': settings.API_URL})
def incio2(request):
    return render(request, 'new_user_wherehouse.html', {'api_url': settings.API_URL})
def listUsers(request):
    return render(request, 'list_users.html', {'api_url': settings.API_URL})
def newWereHouse(request):
    return render(request, 'new_werehouse.html', {'api_url': settings.API_URL})
def listWere(request):
    return render(request, 'list_wherehouse.html', {'api_url': settings.API_URL})
def listProducts(request):
    wcapi = API(
        url="https://bazarcinema.com",  # Cambia esto por la URL de tu tienda WooCommerce
        consumer_key="ck_287291723cb2b4bd87098b9a8378d76a63929744",  # Cambia esto por tu consumer key real
        consumer_secret="cs_b2bff59d498a165fb15cf17697ac225da8cb9e76",  # Cambia esto por tu consumer secret real
        wp_api=True,
        version="wc/v3",
    )
    response = wcapi.get("products")
    products = response.json() if response.status_code == 200 else []

    return render(request, 'list_products.html', {'products': products})