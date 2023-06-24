from django.contrib import admin
from django.urls import path
from Apps.Academica.views import formularioContacto, contactar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', formularioContacto, name='formularioContacto'),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar, name='contactar'),  # Agregado el nombre del patrón
]
