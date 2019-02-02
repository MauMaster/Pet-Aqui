from django.conf.urls import url
from django.urls import include, path
from . import views
from .views import (
    index,
    cadastro,
    cadastro_novo,
    cadastro_negocio,
    activate,
    account_activation_sent
    
)

urlpatterns = [
    url(r'^index/$', index, name='sistema_index'),
    url(r'^cadastro/$', cadastro, name='sistema_cadastro'),
    url(r'^cadastro-novo/$', cadastro_novo, name='sistema_cadastro_novo'),
    url(r'^cadastro-negocio/$', cadastro_negocio, name='sistema_cadastro_negocio'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    
]