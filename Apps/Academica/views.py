from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'login.html')



def home(request):
    return render(request, 'home.html')
def formularioContacto(request):
    return render(request, "formularioContacto.html")
def contactar(request):
    if request.method=="POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["testproyectosmacharette@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
