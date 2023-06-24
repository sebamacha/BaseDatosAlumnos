from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
#creacion de la vista formulario con el request

def formularioContacto(request):
    return render(request, "formularioContacto.html")
    #render me indica la respuesta a traves de esa peticion
    #devuelve el formulario contacto


#vista para recibir datos del formulario recibido
def contactar(request):
    if request.method=="POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["testproyectosmacharette@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")