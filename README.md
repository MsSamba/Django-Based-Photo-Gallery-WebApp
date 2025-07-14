# Django Photo Gallery Project


## 🚀 Application Features Implemented

### **Models**
- ✅ **UserProfile**: Extended user model with bio and profile picture
- ✅ **Tag**: Simple tagging system for photos
- ✅ **Photo**: Core model with image, title, description, tags, user association
- ✅ **Like**: Like/dislike system with unique constraints

### **Views & Functionality**
- ✅ **Gallery Home**: Photo browsing with search and filtering
- ✅ **Photo Detail**: Individual photo view with voting system
- ✅ **Photo Upload**: Upload interface with tag assignment
- ✅ **User Profiles**: Profile viewing and editing
- ✅ **Authentication**: Login, registration, logout
- ✅ **AJAX Voting**: Like/dislike functionality
- ✅ **Search & Filter**: By tags and photo titles

### **Templates & UI**
- ✅ **Modern Responsive Design**: Using Tailwind CSS
- ✅ **Base Template**: Comprehensive navigation with Alpine.js
- ✅ **Gallery Home**: Masonry-style photo grid with filters
- ✅ **Photo Detail**: Full photo view with voting interface
- ✅ **Upload Interface**: Drag-and-drop photo upload
- ✅ **User Profile Pages**: Profile editing and photo collections
- ✅ **Authentication Pages**: Modern login/register forms

### **Forms**
- ✅ **PhotoUploadForm**: File upload with tag selection
- ✅ **User/Profile Update Forms**: Profile editing
- ✅ **Custom User Creation**: Registration form

### **URL Configuration**
- ✅ **Complete URL patterns** for all views
- ✅ **AJAX endpoints** for voting
- ✅ **Media file serving** configured

## 🛠 Technical Stack

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL 17 with psycopg2-binary 2.9.10
- **Frontend**: Tailwind CSS + Alpine.js
- **Image Processing**: Pillow 10.4.0
- **Configuration**: python-decouple 3.8
- **Python Version**: 3.13.3

## 📁 Project Structure

```
photo_gallery/
├── photo_gallery/           # Main project settings
├── photo_gallery_app/       # Main application
│   ├── models.py            # UserProfile, Tag, Photo, Like models
│   ├── views.py             # All view logic implemented
│   ├── forms.py             # Upload and profile forms
│   ├── urls.py              # URL configuration
│   ├── admin.py             # Admin interface setup
│   ├── signals.py           # User profile creation signals
│   ├── templates/           # All HTML templates
│   │   ├── base.html        # Base template with navigation
│   │   └── photo_gallery_app/
│   │       ├── gallery_home.html
│   │       ├── photo_detail.html
│   │       ├── photo_upload.html
│   │       ├── profile.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── user_photos.html
│   └── migrations/          # Database migrations
├── media/                   # User uploads
│   ├── photos/              # Photo uploads
│   ├── profile_pics/        # Profile pictures
│   └── default.jpg          # Default profile image
├── requirements.txt         # Dependencies
└── manage.py               # Django management
```

## 🚀 Key Features Highlights

### **User Experience**
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, intuitive interface with smooth animations
- **AJAX Interactions**: Real-time like/dislike without page refresh
- **Search & Filter**: Easy photo discovery by tags and titles
- **Drag & Drop Upload**: Modern file upload experience

### **Photo Management**
- **Tag System**: Organize photos with multiple tags
- **User Ownership**: Users can manage their own photos
- **Like/Dislike System**: Community engagement features
- **Image Processing**: Automatic profile picture resizing

### **Security & Authentication**
- **User Authentication**: Complete login/registration system
- **Profile Management**: Users can update their profiles
- **Secure File Uploads**: Proper image validation
- **CSRF Protection**: Built-in Django security features

