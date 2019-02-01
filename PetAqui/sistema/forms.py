from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import (
    Usuario,
    Negocio
)

PET_CHOICES = (
    ('dog','Cachorro'), ('cat','Gato'), ('bird', 'Pássaros'), ('fish','Peixes'), ('rep','Reptéis'), ('horse','Cavalos'), ('rat','Roedores')
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
    ('M','Masculino'), ('F','Feminino')
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
                                            'placeholder': 'Email Válido' , 'id': 'email'}))
     email2 = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Repita seu email', 'id': 'email2'}))
     cpf = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder':'000.000.000-00', 'class': 'cpf'} ))
     telefone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                           'placeholder':'(00)0000-0000', 'class': 'phone_with_ddd'}))
                                            
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
                                            'placeholder':'00000-000', 'class': 'cep'}))

     password1  = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password1'}))

     password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password2', 'label': 'Repita a senha'}))

     data_nascimento = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder':'00/00/000', 'class': 'data'}))

     pet = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, choices=PET_CHOICES,)
                                     
     foto = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple':'False' }))

     sexo = forms.ChoiceField( choices=SEXO_CHOICES)

     estado = forms.ChoiceField( choices=STATE_CHOICES)
            
    
     class Meta:
        model = User
        fields = ( 'username', 'email', 'email2',  'telefone', 'data_nascimento', 'sexo', 'foto','endereco', 'numero','bairro','cidade', 'estado',   'cep',  'pet')
       
        

     
       


class NegocioForm(forms.ModelForm):
     class Meta:
        model = Negocio
        fields = '__all__'