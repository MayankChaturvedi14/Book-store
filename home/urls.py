
from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("Registration", views.SignUP, name='Registration'),
     path("LogIn", views.LogIn, name='LogIn'),
    path("Books",views.Books,name='Books'),
    path('signout', views.signout,name="signout"),
    
]
