from django.urls import path 
from compras import views

urlpatterns = [
    path('', views.listar_pratos, name='listar_pratos'),
]