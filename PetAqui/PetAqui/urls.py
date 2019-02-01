from django.contrib import admin
from django.urls import path, include
from sistema.views import index
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index),
    path(r'sistema/', include('sistema.urls')),
    
]

