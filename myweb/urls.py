from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from . import *

urlpatterns = [
    path('register', views.signup, name='register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login',auth_views.LoginView.as_view(template_name='myweb/login.html'),name='login'),
    path('', views.index, name='index'),
    path('home1', views.home1, name='home1'),

]