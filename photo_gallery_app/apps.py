from django.apps import AppConfig


class PhotoGalleryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo_gallery_app'
    
    def ready(self):
        import photo_gallery_app.signals