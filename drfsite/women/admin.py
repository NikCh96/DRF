from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time_create', 'is_published')

admin.site.register(Women, WomenAdmin)

admin.site.register(Category)
