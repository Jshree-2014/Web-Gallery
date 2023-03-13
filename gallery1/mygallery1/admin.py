from csv import list_dialects
from django.contrib import admin
from mygallery1.models import User,Gallery,Video

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','user','image','title','date']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','realname','emailid','password']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=['id','user','video','title','date']