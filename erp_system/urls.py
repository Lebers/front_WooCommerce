from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main.views import login_session, home, api_proxy,api_login,api_proxy_wc
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_session, name='login_session'),
    path('home', home, name='home'),

    path('api_proxy/', api_proxy),
    path('api_proxy_wc/', api_proxy_wc),
    path('api_login', api_login),
    path('inicio/', views.incio, name='inicio'),

    path('', include('main.urls')),

    path('logout/', auth_views.LogoutView.as_view(next_page='login_session'), name='logout'),
    
    path('dashboard/', include('dashboard.urls')),
    path('usuario/', include('usuario.urls')),
    path('pedidos/', include('pedidos.urls')),

    path('product/', views.product, name='product_overview'),
    path('product/<int:id>/', views.product, name='product'),
    
    
    path('listProduct/', views.listProduct, name='product'),


    path('newUser/', views.newUser, name='newUser'),
    path('listUsers/', views.listUsers, name='listUsers'),
    path('listWere/', views.listWere, name='listWere'),
    path('listProducts/', views.listProducts, name='listProducts'),
    path('newWereHouse/', views.newWereHouse, name='newWereHouse'),


    path('specialCatalogs', views.specialCatalogs, name='specialCatalogs'),
    path('specialCatalogs/<str:catalogoName>/', views.specialCatalogs, name='specialCatalogs'),




]