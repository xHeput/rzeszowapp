from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'form.html', {})
