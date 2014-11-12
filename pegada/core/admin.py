from django.contrib import admin

from .models import AppUser, Shoe

admin.site.register(AppUser)
admin.site.register(Shoe)
