
from django.contrib import admin
from django.urls import path
from Apps.Academica.views import formularioContacto, contactar, login_view, home, logout_view
from django.conf.urls.static import static
from django.conf import settings
from Apps.Academica.views import logout_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar, name='contactar'),
    path('logout/', logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
