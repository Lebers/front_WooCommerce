import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
import base64




def new_user(request, username):
    context = {
        'api_url': settings.API_URL,
        'username': username
    }
    return render(request, 'new_user.html', context)



def login_session(request):
    return render(request, 'login.html', {'api_url': settings.API_URL})

@login_required
def home(request):
    #username = "feber"
    username = request.session.get('username', '{User}')
    return render(request, 'home.html', {'api_url': settings.API_URL, 'username': username})

@csrf_exempt
def api_proxys(request):
    data = request.POST

    # Ahora puedes acceder a 'data' sin problemas
    method = data.get('type_method', 'GET')  # 'GET' como valor por defecto si 'type_method' no está presente
    api_method = data.get('api_method')

    api_url = settings.API_URL
    final_url = f"{api_url}/{api_method}"

    # Construye request_data con todos los elementos de data excepto 'api_method'
    request_data = {key: value for key, value in data.items() if key not in ['api_method', 'type_method']}

    # Accede al token de la sesión
    token = request.session.get('auth_token')
    headers = {'Authorization': f"Bearer {token}"}

    # Realiza la solicitud al API externo, ajusta según si es GET o POST
    if method == 'POST':
        response = requests.post(final_url, data=request_data,  headers=headers)
    else:
        response = requests.get(final_url, params=request_data, headers=headers)

    return HttpResponse(response.content, content_type=response.headers['Content-Type'], status=response.status_code)

@csrf_exempt
def api_proxy(request):
    # Asumiendo que estás enviando una petición POST con datos JSON
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

        api_method = data.get('api_method')
        method = data.get('type_method', 'POST')

        api_url = settings.API_URL
        final_url = f"{api_url}/{api_method}"

        # Construye request_data con todos los elementos de data
        request_data = {key: value for key, value in data.items() if key not in ['api_method', 'type_method']}

        token = request.session.get('auth_token')
        headers = {'Authorization': f"Bearer {token}"}

        if method.upper() == 'POST':
            response = requests.post(final_url, json=request_data, headers=headers)
        else:
            response = requests.get(final_url, params=request_data, headers=headers)

        return HttpResponse(response.content, content_type=response.headers['Content-Type'], status=response.status_code)

    return HttpResponse("Unsupported method", status=405)

@csrf_exempt
def api_proxy_wc(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

        api_method = data.get('api_method', 'products')  # Asegúrate de que esto llegue correctamente formado
        type_method = data.get('type_method', 'POST').upper()

        # URL base de WooCommerce
        api_url = "https://bazarcinema.com/"
        consumer_key = "ck_287291723cb2b4bd87098b9a8378d76a63929744"
        consumer_secret = "cs_b2bff59d498a165fb15cf17697ac225da8cb9e76"

        # Codificar las credenciales para autenticación básica
        credentials = f"{consumer_key}:{consumer_secret}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'  # Ejemplo de User-Agent
        }

        # Construye la URL final dependiendo del método API
        final_url = f"{api_url}{api_method}"

        # Determina el método HTTP y hace la petición
        if type_method == 'POST':
            response = requests.post(final_url, json=data, headers=headers)
        elif type_method == 'GET':
            response = requests.get(final_url, params=data, headers=headers)
        elif type_method == 'PUT':
            response = requests.put(final_url, json=data, headers=headers)
        else:
            return HttpResponse("Unsupported HTTP method", status=405)

        # Devolver la respuesta al cliente
        #return HttpResponse(response.content, content_type=response.headers['Content-Type'], status=response.status_code)
        return JsonResponse(response.json(), safe=False, status=response.status_code)


    return HttpResponse("Unsupported method", status=405)


@csrf_exempt
def api_login(request):
    usernameD = request.POST.get('username')
    method = request.method
    api_url = settings.API_URL

    if method == 'POST':
        data = request.POST
    else:
        data = request.GET 

    api_method = data.get('api_method')
    
    final_url = f"{api_url}/{api_method}"

    # Construye request_data con todos los elementos de data excepto 'api_method'
    request_data = {key: value for key, value in data.items() if key != 'api_method'}

    response = requests.post(final_url, data=request_data, json=request_data )
    response_data = response.json()

    if response.status_code == 200:
        # Suponiendo que tu API devuelve una respuesta positiva para un login exitoso
        try:
            token = response_data['data']['token']

            # Almacena el token en la sesión
            request.session['auth_token'] = token
            user, created = User.objects.get_or_create(username=usernameD)
            if created:
                # Establece una contraseña o cualquier otro campo necesario aquí
                user.set_unusable_password()  # Importante si no estás sincronizando contraseñas
                user.save()
            login(request, user)

            # Guardar el nombre de usuario en la sesión para su uso posterior
            request.session['username'] = usernameD  # Almacenar el nombre de usuario en la sesión

            return HttpResponse(response.content, content_type=response.headers['Content-Type'], status=response.status_code)
        except User.DoesNotExist:
            # Crea un nuevo usuario en Django si es necesario o maneja según la política de tu aplicación
            return HttpResponse("Usuario no encontrado en Django, pero autenticado en API externa.", status=404)
    else:
        return HttpResponse(response.content, content_type=response.headers['Content-Type'], status=response.status_code)
    

def menu_crea(request):
    return render(request, 'menu_crea.html', {'api_url': settings.API_URL})
def menu_asocia(request):
    return render(request, 'menu_asocia.html', {'api_url': settings.API_URL})
def catalogo_crea(request):
    return render(request, 'catalogo_crea.html', {'api_url': settings.API_URL})



