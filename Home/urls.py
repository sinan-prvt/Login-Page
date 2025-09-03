from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginn, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
]
