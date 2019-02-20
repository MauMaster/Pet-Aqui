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
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse



from .models import (
    Usuario, 
    Negocio
)

from .forms import (
    UsuarioForm, 
    NegocioForm
)

def profile_detail(request, username):
    if User.objects.get(username__iexact=username):
        user_details = User.objects.get(username__iexact=username)
        return render(request, "profile.html", {
            "user_details": user_details,
        })
    else:
        return render("User not found")


def index(request):
    usuario = Usuario.objects.all()
    form = UsuarioForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'index.html', data)

def perfil(request):
    usuario = Usuario.objects.all()
    form = UsuarioForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'perfil.html', data)
    


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
            username = form.cleaned_data.get('username')
            user.username = username.lower()
            user.save()
            current_site = get_current_site(request)
            subject = 'Ative seu registro no PetAqui'
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


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


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
        return render(request, 'account_activation.html')
    else:
        return render(request, 'account_activation_invalid.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Corriga os erros.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def cadastro_negocio(request):
    negocio = Negocio.objects.all()
    form = NegocioForm()
    data = {'negocio': negocio, 'form': form}
    return render(request, 'cadastro_negocio.html', data)
