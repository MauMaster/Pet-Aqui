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


from .models import (
    Usuario,
    Negocio,
    Gallery
)

PET_CHOICES = (
    ('dog', 'Cachorro'), ('cat', 'Gato'), ('bird', 'Pássaros'), ('fish',
     'Peixes'), ('rep', 'Reptéis'), ('rat', 'Roedores')
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
SEXO_CHOICES = (
    ('M', 'Masculino'), ('F', 'Feminino')
)

HOUR_CHOICES = (
    ('N','Não'), ('S','Sim')
)

class UsuarioForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = "Repita a senha"
        self.fields["password2"].label = "Repita o email"
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

     pet = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, choices=PET_CHOICES, )

     foto = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': 'False'}))

     sexo = forms.ChoiceField(choices=SEXO_CHOICES)

     estado = forms.ChoiceField(choices=STATE_CHOICES)

     about = forms.CharField(
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "7", 'placeholder': 'Uma breve descrição sobre você'}))

     class Meta:
        model = User
        fields = ('username', 'email', 'email2',  'telefone', 'data_nascimento', 'sexo', 'foto',
                  'endereco', 'numero', 'bairro', 'cidade', 'estado',   'cep',  'pet', 'about')
        labels = {
              "username": "Nome de usúario"
       }


class NegocioForm(forms.ModelForm):

     horario_segunda1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_segunda2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_segunda3 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_segunda4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     segunda_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_terca1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_terca2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_terca3 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_terca4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     terca_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_quarta1 = forms.TimeField(required=False, label='Abre', widget=TimePickerInput(format='%I:%M'))
     horario_quarta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_quarta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quarta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     quarta_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_quinta1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quinta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_quinta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_quinta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     quinta_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_sexta1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sexta2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_sexta3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sexta4 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     sexta_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_sabado1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado2 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_sabado4 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     sabado_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)

     horario_domingo1 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_domingo2 = forms.TimeField(required=False, label='Fecha', widget=TimePickerInput(format='%I:%M'))
     horario_domingo3 = forms.TimeField(required=False, label='Abre',  widget=TimePickerInput(format='%I:%M'))
     horario_domingo4 = forms.TimeField(required=False, label='Fecha',  widget=TimePickerInput(format='%I:%M'))
     domingo_24 = forms.ChoiceField(required=False, label='24 Horas', choices=HOUR_CHOICES)
     data = forms.DateField( label='Ano de Inauguração',  widget=DatePickerInput(format='%Y'))

     sobre = forms.CharField(label='História da empresa',
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "7", 'placeholder': 'Uma breve descrição sobre a empresa'}))
     class Meta:
        model = Negocio
        fields = '__all__'
        
        labels = {
            
            
        }

class GalleryForm(forms.ModelForm):
     gallery = forms.FileField(
              widget=forms.ClearableFileInput(attrs={'multiple': 'True'}))
     titulo = forms.CharField()

     class Meta:
        model = Gallery
        fields = ( 'gallery', 'titulo')

     def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(GalleryForm, self).__init__(*args, **kwargs)

     def save(self, commit=True, user=None):
         form = super(GalleryForm, self).save(commit=False)
         form.usario_id = user
         if commit:
            form.save()
         return form