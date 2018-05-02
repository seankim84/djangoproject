from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    
    list_display = ( #if u want to modify, u can use this.(list_display_links)
    #what's different between list_display and list_display_links? = if u have "id" u have to use list_display.
        'creator', #"Comma"!! Don't forget it! 
        'to',
        'notifications_type',
    )

