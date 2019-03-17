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
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404



from .models import (
    Usuario, 
    Negocio,
    Gallery
)

from .forms import (
    UsuarioForm, 
    NegocioForm,
    GalleryForm
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
    gallery = Gallery.objects.all()
    form2 = GalleryForm()
    data2 = {'gallery': gallery, 'form2': form2}
    return render(request, 'perfil.html', data, data2)



def gallery(request):
    gallery = Gallery.objects.all()
    form = GalleryForm()
    data = {'gallery': gallery, 'form': form}
    return render(request, 'gallery.html', data)   

    

def gallery_novo(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            my_novo_gallery = form.save(commit=False)  #save no commit
            my_novo_gallery.user=request.user          #set user
            my_novo_gallery.save()                     #save to db
            return redirect('sistema_perfil')
    else:
        form = GalleryForm
    return render(request, 'gallery.html', {'form': form})


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
            user.usuario.about = form.cleaned_data.get('about')
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

class PhotoUpdate(LoginRequiredMixin, UpdateView):
    model= Usuario  
    fields = ['foto']
    template_name='profile/change-photo.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.usuario.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj


    def get_success_url(self):
        return reverse('sistema_perfil')
        
class UserNameUpdate(LoginRequiredMixin, UpdateView):
    model= User 
    fields = ['username']
    template_name='profile/change-username.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.usuario.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj


    def get_success_url(self):
        return reverse('sistema_perfil')


class EmailUpdate(LoginRequiredMixin, UpdateView):
    model= Usuario
    fields = ['email']
    template_name='profile/change-email.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.usuario.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj


    def get_success_url(self):
        return reverse('sistema_perfil')

class PetUpdate(LoginRequiredMixin, UpdateView):
    model= Usuario
    fields = ['pet']
    template_name='profile/change-pet.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.usuario.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj


    def get_success_url(self):
        return reverse('sistema_perfil')

class DataUpdate(LoginRequiredMixin, UpdateView):
    model= Usuario
    fields = ['nome','sobrenome','cpf','telefone','data_nascimento','sexo','endereco','numero','bairro','cidade','estado', 'cep']
    template_name='profile/change-data.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.usuario.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj


    def get_success_url(self):
        return reverse('sistema_perfil')

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

def cadastro_negocio_novo(request): 
    if request.method == 'POST':
        form = NegocioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.negocio.empresa = form.cleaned_data.get('empresa')
            
            user.negocio.cnpj = form.cleaned_data.get('cnpj')
            user.negocio.telefone = form.cleaned_data.get('telefone')
            user.negocio.whatsapp = form.cleaned_data.get('whatsapp')
            user.negocio.email = form.cleaned_data.get('email')
            user.negocio.site = form.cleaned_data.get('site')
            user.negocio.foto = form.cleaned_data.get('foto')
            user.negocio.tipo = form.cleaned_data.get('tipo')
            user.negocio.pet_aceitos = form.cleaned_data.get('pet_aceitos')
            user.negocio.endereco = form.cleaned_data.get('endereco')
            user.negocio.numero = form.cleaned_data.get('numero')
            user.negocio.bairro = form.cleaned_data.get('bairro')
            user.negocio.cep = form.cleaned_data.get('cep')
            user.negocio.cidade = form.cleaned_data.get('cidade')
            user.negocio.estado = form.cleaned_data.get('estado')
            user.negocio.segunda = form.cleaned_data.get('segunda')
            user.negocio.horario_segunda1 = form.cleaned_data.get('horario_segunda1')
            user.negocio.horario_segunda2 = form.cleaned_data.get('horario_segunda2')
            user.negocio.horario_segunda3 = form.cleaned_data.get('horario_segunda3')
            user.negocio.horario_segunda4 = form.cleaned_data.get('horario_segunda4')
            user.negocio.segunda_24 = form.cleaned_data.get('segunda_24')
            user.negocio.terca = form.cleaned_data.get('terca')
            user.negocio.horario_terca1 = form.cleaned_data.get('horario_terca1')
            user.negocio.horario_terca2 = form.cleaned_data.get('horario_terca2')
            user.negocio.horario_terca3 = form.cleaned_data.get('horario_terca3')
            user.negocio.horario_terca4 = form.cleaned_data.get('horario_terca4')
            user.negocio.terca_24 = form.cleaned_data.get('terca_24')
            user.negocio.quarta = form.cleaned_data.get('quarta')
            user.negocio.horario_quarta1 = form.cleaned_data.get('horario_quarta1')
            user.negocio.horario_quarta2 = form.cleaned_data.get('horario_quarta2')
            user.negocio.horario_quarta3 = form.cleaned_data.get('horario_quarta3')
            user.negocio.horario_quarta4 = form.cleaned_data.get('horario_quarta4')
            user.negocio.quarta_24 = form.cleaned_data.get('quarta_24')
            user.negocio.quinta = form.cleaned_data.get('quinta')
            user.negocio.horario_quinta1 = form.cleaned_data.get('horario_quinta1')
            user.negocio.horario_quinta2 = form.cleaned_data.get('horario_quinta2')
            user.negocio.horario_quinta3 = form.cleaned_data.get('horario_quinta3')
            user.negocio.horario_quinta4 = form.cleaned_data.get('horario_quinta4')
            user.negocio.quinta_24 = form.cleaned_data.get('quinta_24')
            user.negocio.sexta = form.cleaned_data.get('sexta')
            user.negocio.horario_sexta1 = form.cleaned_data.get('horario_sexta1')
            user.negocio.horario_sexta2 = form.cleaned_data.get('horario_sexta2')
            user.negocio.horario_sexta3 = form.cleaned_data.get('horario_sexta3')
            user.negocio.horario_sexta4 = form.cleaned_data.get('horario_sexta4')
            user.negocio.sexta_24 = form.cleaned_data.get('sexta_24')
            user.negocio.sabado = form.cleaned_data.get('sabado')
            user.negocio.horario_sabado1 = form.cleaned_data.get('horario_sabado1')
            user.negocio.horario_sabado2 = form.cleaned_data.get('horario_sabado2')
            user.negocio.horario_sabado3 = form.cleaned_data.get('horario_sabado3')
            user.negocio.horario_sabado4 = form.cleaned_data.get('horario_sabado4')
            user.negocio.sabado_24 = form.cleaned_data.get('sabado_24')
            user.negocio.domingo = form.cleaned_data.get('domingo')
            user.negocio.horario_domingo1 = form.cleaned_data.get('horario_domingo1')
            user.negocio.horario_domingo2 = form.cleaned_data.get('horario_domingo2')
            user.negocio.horario_domingo3 = form.cleaned_data.get('horario_domingo3')
            user.negocio.horario_domingo4 = form.cleaned_data.get('horario_domingo4')
            user.negocio.domingo_24 = form.cleaned_data.get('domingo_24')
            user.negocio.sobre = form.cleaned_data.get('sobre')
            user.negocio.password1 = form.cleaned_data.get('password1')
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
        form = NegocioForm()
    return render(request, 'cadastro_negocio.html', {'form': form})
