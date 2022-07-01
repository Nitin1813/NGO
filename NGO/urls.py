from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns=[
    path('',views.Home, name="index"),
    path('Home', views.Home, name="home"),
    path('About.html', views.About , name="About"),
    path('Donate.html', views.Donate, name="Donate"),
    path('Gallery.html', views.Gallery, name="Gallery"),
    path('success' , views.success , name='success'),
    path('login', views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('logout',views.logout, name="logout"),
    path('donate1.html',views.donate1, name="donate1"),
    path('logedin',views.logedin,name="logedin")
]

