from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'form.html', {})

def login_user(request):
    return render(request, 'login.html', {})

def statute(request):
    return render(request,'statute.html',{})

def panel_user(request):
    return render(request,'panel.html',{})