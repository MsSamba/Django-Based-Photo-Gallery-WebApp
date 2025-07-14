# photo_gallery_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.redirect_to_login),  # redirects to /login/
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='photo_gallery_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

]
