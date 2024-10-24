from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    path('registration-success/', views.registration_success_view, name='registration_success'),
    path('login-success/', views.login_success_view, name='login_success'),
]
