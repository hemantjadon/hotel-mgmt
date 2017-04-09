from django.contrib import admin
from .models import Staff, Manager, Worker, Department

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_balance</i>'

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment_ind</i>'

@admin.register(Worker)
class RoomAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_box</i>'
