from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('nombre_de_la_ruta_a_la_pagina_principal')
        else:
            # Mostrar mensaje de error al usuario
            pass
    return render(request, 'accounts/login.html')

