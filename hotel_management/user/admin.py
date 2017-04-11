from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import AuthUser
from .forms import AuthUserChangeForm, AuthUserCreationForm

# Register your models here.

'''
    Custom user admin for the application.
'''

@admin.register(AuthUser)
class AuthUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('User Information', {'fields': ('age', 'phone_number')}),
    )
    add_fieldsets = (
      (None, {'fields':('username','password1','password2','first_name','last_name','email', 'phone_number', 'age'),}),)
    add_form = AuthUserCreationForm
    form = AuthUserChangeForm
    icon = '<i class="material-icons">person</i>'

admin.site.unregister(Group)
