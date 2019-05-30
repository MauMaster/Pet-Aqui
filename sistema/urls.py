from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from .views import (
    index,
    cadastro,
    cadastro_novo,
    cadastro_negocio,
    cadastro_negocio_novo,
    activate,
    account_activation_sent,
    perfil,
    profile_detail,
    change_password,
    PetEmpresaUpdate,
    PhotoEmpresaUpdate,
    EmailEmpresaUpdate,
    search,
    search_usuario,
    BasicUploadView,
    delete,
    cadastro_comentario,
    comentario_form,
    comentario_form_empresa,
    cadastro_comentario_empresa,
    delete_comentario
    
    
)

urlpatterns = [
    url(r'^index/$', index, name='sistema_index'),
    url(r'^search-usuario/$', views.search_usuario, name='search_usuario'),
    url(r'^search/$', views.search, name='search'),
    url(r'^cadastro/$', cadastro, name='sistema_cadastro'),
    url(r'perfil/$', perfil, name='sistema_perfil'),
    url(r'^cadastro-novo/$', cadastro_novo, name='sistema_cadastro_novo'),
    url(r'^cadastro-negocio/$', cadastro_negocio, name='sistema_cadastro_negocio'),
    url(r'^cadastro-negocio-novo/$', cadastro_negocio_novo, name='sistema_cadastro_negocio_novo'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^cadastro-comentario/(?P<username>[\w.@+-]+)/$', cadastro_comentario, name='cadastro_comentario'),
    url(r'^comentario/(?P<username>[\w.@+-]+)/$', comentario_form, name='comentario_form'),
    url(r'^cadastro-comentario-empresa/(?P<username>[\w.@+-]+)/$', cadastro_comentario_empresa, name='cadastro_comentario_empresa'),
    url(r'^comentario-empresa/(?P<username>[\w.@+-]+)/$', comentario_form_empresa, name='comentario_form_empresa'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile_detail, name='profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^change-photo/$', views.PhotoUpdate.as_view(), 
     name='sistema_change_photo'),
    url(r'^change-username/$', views.UserNameUpdate.as_view(), 
     name='sistema_change_username'),
    url(r'^change-email/$', views.EmailUpdate.as_view(), 
     name='sistema_change_email'),
    url(r'^change-data/$', views.DataUpdate.as_view(), 
     name='sistema_change_data'),
    url(r'^change-pet/$', views.PetUpdate.as_view(), 
     name='sistema_change_pet'),
    url(r'^change-data-negocio/$', views.DataUpdateNegocio.as_view(), 
     name='sistema_change_data_negocio'),
    url(r'^change-hora/$', views.HoraUpdateNegocio.as_view(), 
     name='sistema_change_hora'),
    url(r'^change-pet-empresa/$', views.PetEmpresaUpdate.as_view(), 
     name='sistema_change_pet_empresa'),
    url(r'^change-foto-empresa/$', views.PhotoEmpresaUpdate.as_view(), 
     name='sistema_change_foto_empresa'),
    url(r'^change-email-empresa/$', views.EmailEmpresaUpdate.as_view(), 
     name='sistema_change_email_empresa'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^delete-comentario/(?P<id>\d+)/$', views.delete_comentario, name='delete_comentario'),
   
   
     
    
]
