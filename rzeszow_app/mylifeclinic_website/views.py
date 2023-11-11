from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'form.html', {})

def login_user(request):
    # Chack to see if logging in
    if request.method == 'POST':
        username = request.POST['emaile']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Zalogowano pomyślnie!")
            return redirect('panel')
        else:
            messages.success(request, "Wystąpił błąd podczas logowania, spróbuj ponownie...")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie...")
    return redirect('home')

def statute(request):
    return render(request,'statute.html',{})

def panel_user(request):
    return render(request,'panel.html',{})