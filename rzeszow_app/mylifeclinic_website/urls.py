from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('form/', views.register_user, name = 'form'),
    path('login/', views.login_user, name = 'login'),
    path('statute/',views.statute, name='statute'),
]