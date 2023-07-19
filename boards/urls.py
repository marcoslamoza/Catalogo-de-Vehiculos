from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro_view, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('vehiculos/add', views.formulario_view, name="formulario"),
    path('', views.Index, name="index"),
    path('listado/', views.listado, name="listado"),
]
