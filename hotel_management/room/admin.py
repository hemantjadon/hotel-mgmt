from django.contrib import admin
from .models import Room

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">room</i>'
