# photo_gallery/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PhotoUploadForm
from .models import Photo, Tag, Like, UserProfile
from django.contrib.auth.models import User


def redirect_to_login(request):
    return redirect('login')

def gallery_home(request):
    """Homepage displaying all photos with optional filtering"""
    photos = Photo.objects.all()
    tags = Tag.objects.all()
    
    # Filter by tag if provided
    tag_filter = request.GET.get('tag')
    if tag_filter:
        photos = photos.filter(tags__name=tag_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        photos = photos.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(photos, 12)  # Show 12 photos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'tags': tags,
        'current_tag': tag_filter,
        'search_query': search_query,
    }
    return render(request, 'photo_gallery_app/gallery_home.html', context)


def photo_detail(request, pk):
    """Detailed view of a single photo"""
    photo = get_object_or_404(Photo, pk=pk)
    user_like = None
    
    if request.user.is_authenticated:
        try:
            user_like = Like.objects.get(user=request.user, photo=photo)
        except Like.DoesNotExist:
            pass
    
    context = {
        'photo': photo,
        'user_like': user_like,
        'likes_count': photo.likes_count(),
        'dislikes_count': photo.dislikes_count(),
    }
    return render(request, 'photo_gallery_app/photo_detail.html', context)


@login_required
def photo_upload(request):
    """Upload a new photo"""
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('photo-detail', pk=photo.pk)
    else:
        form = PhotoUploadForm()
    
    return render(request, 'photo_gallery_app/photo_upload.html', {'form': form})


@login_required
@require_POST
def toggle_like(request, pk):
    """Ajax view to handle like/dislike functionality"""
    photo = get_object_or_404(Photo, pk=pk)
    is_like = request.POST.get('is_like') == 'true'
    
    like, created = Like.objects.get_or_create(
        user=request.user,
        photo=photo,
        defaults={'is_like': is_like}
    )
    
    if not created:
        if like.is_like == is_like:
            # Remove like/dislike if clicking the same button
            like.delete()
            action = 'removed'
        else:
            # Toggle between like and dislike
            like.is_like = is_like
            like.save()
            action = 'liked' if is_like else 'disliked'
    else:
        action = 'liked' if is_like else 'disliked'
    
    return JsonResponse({
        'action': action,
        'likes_count': photo.likes_count(),
        'dislikes_count': photo.dislikes_count(),
    })


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'photo_gallery_app/register.html', {'form': form})


@login_required
def profile(request):
    """User profile view with edit functionality"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    
    # Get user's uploaded photos
    user_photos = Photo.objects.filter(uploaded_by=request.user)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_photos': user_photos,
    }
    return render(request, 'photo_gallery_app/profile.html', context)


def user_photos(request, username):
    """View all photos uploaded by a specific user"""
    user = get_object_or_404(User, username=username)
    photos = Photo.objects.filter(uploaded_by=user)
    
    # Pagination
    paginator = Paginator(photos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'photos_user': user,
    }
    return render(request, 'photo_gallery_app/user_photos.html', context)
