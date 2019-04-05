
import django_filters
from django import forms
from .models import (
    Negocio,
    Usuario
)




class NegocioFilter(django_filters.FilterSet):
    
    cidade  = django_filters.CharFilter(lookup_expr='icontains')
    
    telefone  = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = Negocio
        fields = ['cidade', 'estado', 'pet_aceitos', 'tipo', 'telefone', ]


class UsuarioFilter(django_filters.FilterSet):
    nome  = django_filters.CharFilter(lookup_expr='icontains')
    sobrenome  = django_filters.CharFilter(lookup_expr='icontains')
    email  = django_filters.CharFilter(lookup_expr='icontains')
    cidade  = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'estado', 'cidade']
