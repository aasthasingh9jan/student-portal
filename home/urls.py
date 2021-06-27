from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name='contact'),
    path('review/',views.review,name='review'),
    path('quora/',views.quora,name='quora'),
    path('pyq/',views.pyq,name='pyq'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]