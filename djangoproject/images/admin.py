from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display_links = ( #if u want to modify, u can use this.(list_display_links)
        'location', #"Comma"!! Don't forget it! 
        'caption', 
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = ( #Filtering like lowers and show this on the right side
        'location',
        'creator',
    ) 

    list_display = ( #admin django documentation
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (    
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )