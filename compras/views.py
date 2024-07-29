from django.shortcuts import render
from .models import Prato, Categoria

def listar_pratos(request):
    pratos = Prato.objects.all() # Query com todos os pratos
    categorias = Categoria.objects.all() # Query com todas as categorias

    context = {'lista_pratos': pratos, 'lista_categorias': categorias}
    return render(request, 'index.html', context)