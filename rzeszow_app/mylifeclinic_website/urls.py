from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('form/', views.register_user, name = 'form'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('statute/',views.statute, name='statute'),
    path('panel/',views.panel_user, name='panel'),
    path('doc_login/',views.doc_user, name='doc_user'),
]