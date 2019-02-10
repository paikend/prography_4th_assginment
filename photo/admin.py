from django.contrib import admin
from .models import *
# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'writer', 'created', 'image', 'updated']
    list_filter = ['writer', 'created', 'updated']
    search_fields = ['text', 'created', 'updated']
    raw_id_fields = ['writer']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)


