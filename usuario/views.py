from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def nuevo_usuario(request):
    return render(request, 'nuevo.html')

@login_required
def buscar(request):
    return render(request, 'buscar.html')

@login_required
def nuevo_usuario_warehouse(request):
    return render(request, 'nuevo_usuario_warehouse.html')
