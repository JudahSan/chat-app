from re import template 
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    # path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
