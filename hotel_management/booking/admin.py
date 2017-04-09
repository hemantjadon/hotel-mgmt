from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">book</i>'
    list_display = ('check_in_date', 'check_out_date', 'room', 'customer', 'customer_points', 'price')
