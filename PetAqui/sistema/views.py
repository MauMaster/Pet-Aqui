from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    Usuario, 
    Negocio
)

from .forms import (
    UsuarioForm, 
    NegocioForm
)



def index(request):
    usuario = Usuario.objects.all()
    form = UsuarioForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'index.html', data)


def cadastro(request):
    usuario = Usuario.objects.all()
    form = UsuarioForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'cadastro.html', data)

def cadastro_novo(request): 
    if request.method == 'POST':
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoas adicionado com sucesso")
            return redirect('sistema_cadastro')
    else:
        form = UsuarioForm
    return render(request, 'cadastro.html', {'form': form})


def cadastro_negocio(request):
    negocio = Negocio.objects.all()
    form = NegocioForm()
    data = {'negocio': negocio, 'form': form}
    return render(request, 'cadastro_negocio.html', data)
