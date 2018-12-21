from django.shortcuts import render, redirect

from .models import (
    Usuario, 
    estabelecimentos
)

from .forms import (
    UsuarioForm, 
    estabelecimentosForm
)



def index(request):
    usuario = Usuario.objects.all()
    form = UsuarioForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'index.html', data)
