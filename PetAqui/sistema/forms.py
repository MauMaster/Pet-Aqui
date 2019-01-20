from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple


from .models import (
    Usuario,
    Negocio
)

class UsuarioForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields["senha2"].label = "Repita a senha"
        self.fields["email2"].label = "Repita o email"
         # pode fazer isso com todos os campos

  
          
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
                                            'placeholder': 'Email Válido' , 'id': 'email'}))
     email2 = forms.CharField(
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
                                            'placeholder': 'numero'}))
                                            
     bairro = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))
     cep = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder':'00000-000', 'class': 'cep'}))

     senha = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'senha'}))

     senha2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'senha2', 'label': 'Repita a senha'}))

     data_nascimento = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder':'00/00/000', 'class': 'data'}))

        
                                            
     
     
     class Meta:
        model = Usuario
        fields = '__all__'
       
        

     
       


class NegocioForm(forms.ModelForm):
     class Meta:
        model = Negocio
        fields = '__all__'
