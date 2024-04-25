from django.shortcuts import render

def nuevo_usuario(request):
    return render(request, 'nuevo.html')

def buscar(request):
    return render(request, 'buscar.html')

def nuevo_usuario_warehouse(request):
    return render(request, 'nuevo_usuario_warehouse.html')
