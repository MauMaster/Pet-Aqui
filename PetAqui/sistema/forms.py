from django.forms import ModelForm
from django import forms

from .models import (
    Usuario,
    Negocio
)

class UsuarioForm(forms.ModelForm):
     class Meta:
        model = Usuario
        fields = '__all__'


class NegocioForm(forms.ModelForm):
     class Meta:
        model = Negocio
        fields = '__all__'
