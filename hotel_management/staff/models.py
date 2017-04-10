from django.db import models
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supervisor = models.ForeignKey('Manager', blank=True, null=True, related_name='managed_by')

    def __str__(self):
        return self.user.username

class Manager(Staff):
    department = models.ForeignKey('Department', blank=False, null=True)

class Worker(Staff):
    department = models.ForeignKey('Department', blank=False, null=True)
