from django.conf.urls import url
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    index,
    cadastro,
    cadastro_novo,
    cadastro_negocio,
    activate,
    account_activation_sent,
    perfil,
    profile_detail
    
)

urlpatterns = [
    url(r'^index/$', index, name='sistema_index'),
    url(r'^cadastro/$', cadastro, name='sistema_cadastro'),
    url(r'perfil/$', perfil, name='sistema_perfil'),
    url(r'^cadastro-novo/$', cadastro_novo, name='sistema_cadastro_novo'),
    url(r'^cadastro-negocio/$', cadastro_negocio, name='sistema_cadastro_negocio'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile_detail, name='profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
