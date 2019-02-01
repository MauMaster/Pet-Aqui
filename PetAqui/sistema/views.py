from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from sistema.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

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
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.usuario.nome = form.cleaned_data.get('nome')
            user.usuario.sobrenome = form.cleaned_data.get('sobrenome')
            user.usuario.email = form.cleaned_data.get('email')
            user.usuario.telefone = form.cleaned_data.get('telefone')
            user.usuario.cidade = form.cleaned_data.get('cidade')
            user.usuario.endereco = form.cleaned_data.get('endereco')
            user.usuario.cpf = form.cleaned_data.get('cpf')
            user.usuario.numero = form.cleaned_data.get('numero')
            user.usuario.bairro = form.cleaned_data.get('bairro')
            user.usuario.cep = form.cleaned_data.get('cep')
            user.usuario.password1 = form.cleaned_data.get('password1')
            user.usuario.data_nascimento = form.cleaned_data.get('data_nascimento')
            user.usuario.pet = form.cleaned_data.get('pet')
            user.usuario.foto = form.cleaned_data.get('foto')
            user.usuario.sexo = form.cleaned_data.get('sexo')
            user.usuario.estado = form.cleaned_data.get('estado')
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.usuario.email_confirmed = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return render(request, 'account_activation_invalid.html')
        
def cadastro_negocio(request):
    negocio = Negocio.objects.all()
    form = NegocioForm()
    data = {'negocio': negocio, 'form': form}
    return render(request, 'cadastro_negocio.html', data)