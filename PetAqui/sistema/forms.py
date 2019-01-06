from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import (
    Usuario,
    Negocio
)
PET_CHOICES = (
    ('dog','Cachorro'), ('cat','Gato'), ('bird', 'Passáros'), ('fish','Peixes'), ('rep','Reptéis'), ('naosei','Cavalos'), ('rat','Roedores')
)


class UsuarioForm(forms.ModelForm):
     nome = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Nome'}))
     sobrenome = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sobrenome'}))
     email = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Email Válido'}))
     email = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Repita seu email'}))
     cpf = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'somente números'}))
     telefone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'somente números'}))
                                            
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
                                            'placeholder': 'numero'}))
                                            
     bairro = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))
     cep = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'somente números'}))

     senha = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos'}))

                                            
     pet =  forms.MultipleChoiceField(choices=PET_CHOICES, widget=forms.CheckboxSelectMultiple)
     
     class Meta:
        model = Usuario
        fields = '__all__'

     def clean(self):
        cleaned_data = super(UsuarioForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        if not nome and not email:
            raise forms.ValidationError('Campos obriatorios')
       


class NegocioForm(forms.ModelForm):
     class Meta:
        model = Negocio
        fields = '__all__'
