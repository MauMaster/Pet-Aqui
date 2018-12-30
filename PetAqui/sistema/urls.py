from django.conf.urls import url
from .views import (
    index,
    cadastro,
    cadastro_negocio
    
)

urlpatterns = [
    url(r'^index/$', index, name='sistema_index'),
    url(r'^cadastro/$', cadastro, name='sistema_cadastro'),
    url(r'^cadastro-negocio/$', cadastro_negocio, name='sistema_cadastro_negocio'),

]