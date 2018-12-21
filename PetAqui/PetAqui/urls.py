from django.contrib import admin
from django.urls import path
from sistema.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index),
]
