from django.contrib import admin
from django.urls import path, include
from sistema.views import index, profile_detail
from django.conf.urls import url
from django.contrib.auth import logout




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path(r'', index),
    path(r'sistema/', include('sistema.urls')),
    path(r'', include('sistema.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

