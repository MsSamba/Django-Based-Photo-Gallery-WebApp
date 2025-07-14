from django.contrib import admin
from .models import Photo, UserProfile, Tag, Like


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    list_filter = ['user__date_joined']
    search_fields = ['user__username', 'user__email']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_by', 'created_at', 'likes_count', 'dislikes_count']
    list_filter = ['created_at', 'tags', 'uploaded_by']
    search_fields = ['title', 'description', 'uploaded_by__username']
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    
    def likes_count(self, obj):
        return obj.likes_count()
    likes_count.short_description = 'Likes'
    
    def dislikes_count(self, obj):
        return obj.dislikes_count()
    dislikes_count.short_description = 'Dislikes'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'is_like', 'created_at']
    list_filter = ['is_like', 'created_at']
    search_fields = ['user__username', 'photo__title']