from django.forms import ModelForm
from django import forms

from .models import (
    Usuario,
    estabelecimentos
)

class UsuarioForm(forms.ModelForm):
     class Meta:
        model = Usuario
        fields = '__all__'


class estabelecimentosForm(forms.ModelForm):
     class Meta:
        model = estabelecimentos
        fields = '__all__'
