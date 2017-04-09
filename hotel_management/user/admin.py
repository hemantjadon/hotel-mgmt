from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import AuthUser

# Register your models here.

'''
    Custom user admin for the application.
'''

@admin.register(AuthUser)
class AuthUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('User Information', {'fields': ('dob', 'phone_number')}),
    )
    icon = '<i class="material-icons">person</i>'

admin.site.unregister(Group)
