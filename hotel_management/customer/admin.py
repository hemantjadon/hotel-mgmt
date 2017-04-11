from django.contrib import admin
from .models import Customer
from .forms import CustomerForm
from booking.models import Booking
from booking.forms import BookingForm

# Register your models here.

class BookinkInline(admin.StackedInline):
    model = Booking
    form = BookingForm
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">loyalty</i>'
    list_display = ('user', 'street', 'city', 'state', 'zip_code', 'id_proof_key', 'points')
    inlines = [BookinkInline]
    form = CustomerForm
