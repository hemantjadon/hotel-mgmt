from django.contrib import admin
from .models import Manager, Worker, Department

# Register your models here.

class ManagerInline(admin.StackedInline):
    model = Manager
    verbose_name = "Manages"
    verbose_name_plural = "Manages"
    fk_name = 'supervisor'
    extra = 0

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_balance</i>'

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment_ind</i>'
    list_display = ('user', 'department', 'supervisor')
    inlines = [ManagerInline]

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_box</i>'
    list_display = ('user', 'department', 'supervisor')
