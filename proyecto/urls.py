from django.contrib import admin
from django.urls import path
from Apps.Academica.views import formularioContacto, contactar, login_view, home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar, name='contactar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
