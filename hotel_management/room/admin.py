from django.contrib import admin
from .models import Room
from booking.models import Booking

# Register your models here.

class BookinkInline(admin.StackedInline):
    model = Booking
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">room</i>'
    list_display = ('room_no', 'floor', 'description')
    inlines = [BookinkInline]
