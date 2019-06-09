from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from django.core.files import File
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from django.db import transaction
from crispy_forms.bootstrap import InlineField


from .models import (
    Usuario,
    Negocio,
    Photo,
    Pets,
    Comentario
)

STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)


PET_CHOICES = (
    ('Cachorro','Cachorro'), ('Gato','Gato'), ('Peixes','Peixes'), ('Tartarugas','Tartarugas'), ('Hamster','Hamster')
)


PETN_CHOICES = (
('Cachorro','Cachorro'), ('Gato','Gato'), ('Cachorro e  Gato','Cachorro e  Gato')
)


SEXO_CHOICES = (
    ('M','Masculino'), ('F','Feminino')
)

TIPO_CHOICES = (
    ('Hotéis','Hotéis'), ('PetShops','PetShops'), ('Veterinários','Veterinários'), ('Restaurantes','Restaurantes'), ('Cafés','Cafés'), ('HotéisPet','HotéisPet'),
)

HOUR_CHOICES = (
    ('Não','Não'), ('Sim','Sim')
)

NOTA_CHOICES = (
    (0,'0'),(1,'1'), (1,'2'), (3,'3'), (4,'4'), (5,'5')
)

class UsuarioForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = "Repita a senha"
        self.fields["password2"].label = "Repita o email"
        self.fields["about"].label = "Sobre você"
        self.fields["username"].label = "Nome de usúario"
         # pode fazer isso com todos os campos

     nome = forms.CharField()
     sobrenome = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sobrenome'}))
     email = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Email Válido', 'id': 'email'}))
     email2 = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Repita seu email', 'id': 'email2'}))
     cpf = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '000.000.000-00', 'class': 'cpf', 'id': 'cpf'}))
     telefone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                           'placeholder': '(00)0000-0000', 'class': 'phone_with_ddd'}))

     cidade = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sua cidade'}))

     endereco = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Rua, Av, Estrada'}))

     numero = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'numero', 'class': 'numero'}))

     bairro = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))
     cep = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00000-000', 'class': 'cep'}))

     password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password1'}))

     password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password2', 'label': 'Repita a senha'}))

     data_nascimento = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00/00/000', 'class': 'data', }))

     pet = forms.ChoiceField(choices=PETN_CHOICES)

     foto = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': 'False'}))
       
    
     sexo = forms.ChoiceField(choices=SEXO_CHOICES)

     estado = forms.ChoiceField(choices=STATE_CHOICES)

     about = forms.CharField(
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "4", 'placeholder': 'Uma breve descrição sobre você', 'id': 'textareaChars', 'maxlength': "255"}))

     class Meta:
        model = User
        fields = ('username', 'email', 'email2',  'telefone', 'data_nascimento', 'sexo', 'foto',
                  'endereco', 'numero', 'bairro', 'cidade', 'estado',   'cep',  'pet', 'about')
        
    

class NegocioForm(UserCreationForm):
     empresa = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Nome da Empresa'}))
     cnpj = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'xx.xxx.xxx/xxxx-xx', 'class': 'cnpj'}))
     email = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Email Válido', 'id': 'email'}))
     email2 = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Repita seu email', 'id': 'email2'}))
     telefone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                           'placeholder': '(00)0000-0000', 'class': 'phone_with_ddd'}))
     whatsapp = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                           'placeholder': '(00)0000-0000', 'class': 'phone_with_ddd'}))
     site = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Site da Empresa'}))
     foto = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': 'False'}))

     tipo = forms.ChoiceField(choices=TIPO_CHOICES)

    

     pet_aceitos = forms.ChoiceField(choices=PETN_CHOICES)



     endereco = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Rua, Av, Estrada'}))
     numero = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'numero', 'class': 'numero'}))
     bairro = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))
     cep = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00000-000', 'class': 'cep'}))
     cidade = cidade = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sua cidade'}))
     estado = forms.ChoiceField(choices=STATE_CHOICES)
     
     sobre = forms.CharField(label='História da empresa',
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "4", 'placeholder': 'Uma breve descrição sobre a empresa', 'id': 'textareaChars', 'maxlength': "255"}))
     password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password1'}))

     password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password2', 'label': 'Repita a senha'}))

     segunda = forms.CharField(initial="Segunda")
     terca = forms.CharField(initial="Terça")
     quarta = forms.CharField(initial="Quarta")
     quinta = forms.CharField(initial="Quinta")
     sexta = forms.CharField(initial="Sexta")
     sabado = forms.CharField(initial="Sábado")
     domingo = forms.CharField(initial="Domingo")

     horario_segunda1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_segunda2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_segunda3 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_segunda4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
    

     horario_terca1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_terca2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_terca3 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_terca4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
    

     horario_quarta1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_quarta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_quarta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quarta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
    

     horario_quinta1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quinta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_quinta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quinta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
  

     horario_sexta1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sexta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_sexta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sexta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
    

     horario_sabado1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado4 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     

     horario_domingo1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_domingo2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_domingo3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_domingo4 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     
     

     
     class Meta:
        model = User
        fields = ('username', 'empresa',   'cnpj', 'telefone', 'whatsapp', 'email',
                  'site', 'foto', 'tipo', 'pet_aceitos', 'endereco',   'numero',  'bairro', 'cep',
                  'cidade', 'estado', 'sobre', 'password1',
                  'segunda', 'horario_segunda1', 'horario_segunda2', 'horario_segunda3', 'horario_segunda4', 
                  'terca', 'horario_terca1', 'horario_terca2', 'horario_terca3', 'horario_terca4',
                  'quarta', 'horario_quarta1', 'horario_quarta2', 'horario_quarta3', 'horario_quarta4',
                  'quinta', 'horario_quinta1', 'horario_quinta2', 'horario_quinta3', 'horario_quinta4',
                  'sexta', 'horario_sexta1', 'horario_sexta2', 'horario_sexta3', 'horario_sexta4',
                  'sabado', 'horario_sabado1', 'horario_sabado2', 'horario_sabado3', 'horario_sabado4',
                  'domingo', 'horario_domingo1', 'horario_domingo2', 'horario_domingo3', 'horario_domingo4')
        
        labels = {
                "username": "Nome de usúario"
                       
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', 'title')

       
class PetsForm(forms.ModelForm):
    pets = forms.MultipleChoiceField(
       widget=forms.CheckboxSelectMultiple, choices=PET_CHOICES )
    class Meta:
        model = Pets
        fields = ('pets', 'user')

class ComentarioForm(forms.ModelForm):
    nota = forms.ChoiceField(choices=NOTA_CHOICES, required=False )
    comentario = forms.CharField(
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "4", 'placeholder': 'Digite seu comentário', 'id': 'textareaChars', 'maxlength': "255"}))
    class Meta:
        model = Comentario
        fields = ('comentario', 'nota')
       


