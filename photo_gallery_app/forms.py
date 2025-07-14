# photo_gallery/forms.py
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile, Photo, Tag


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']


class PhotoUploadForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    new_tags = forms.CharField(
        max_length=200,
        required=False,
        help_text="Add new tags separated by commas"
    )

    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def save(self, commit=True):
        photo = super().save(commit=False)
        
        if commit:
            photo.save()
            
            # Handle new tags
            new_tags_str = self.cleaned_data.get('new_tags')
            if new_tags_str:
                new_tag_names = [tag.strip() for tag in new_tags_str.split(',') if tag.strip()]
                for tag_name in new_tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    photo.tags.add(tag)
            
            # Save existing tags
            self.save_m2m()
        
        return photo
