from django.shortcuts import render
from .forms import PratoForm
from .models import Prato

def listar_pratos(request):
    pratos = Prato.objects.all() # Query com todos objetos da lista

    context = {'lista_pratos': pratos}
    return render(request, 'index.html', context)