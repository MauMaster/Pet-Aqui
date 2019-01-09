from django.conf.urls import url
from .views import (
    index,
    cadastro,
    cadastro_novo,
    cadastro_negocio
    
)

urlpatterns = [
    url(r'^index/$', index, name='sistema_index'),
    url(r'^cadastro/$', cadastro, name='sistema_cadastro'),
    url(r'^cadastro-novo/$', cadastro_novo, name='sistema_cadastro_novo'),
    url(r'^cadastro-negocio/$', cadastro_negocio, name='sistema_cadastro_negocio'),

]
