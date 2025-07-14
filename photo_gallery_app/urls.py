# photo_gallery_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Homepage and gallery
    path('', views.gallery_home, name='gallery-home'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='photo_gallery_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
    
    # Photo functionality
    path('photo/<int:pk>/', views.photo_detail, name='photo-detail'),
    path('photo/upload/', views.photo_upload, name='photo-upload'),
    path('photo/<int:pk>/like/', views.toggle_like, name='toggle-like'),
    path('user/<str:username>/photos/', views.user_photos, name='user-photos'),
]
