'''
    Models related to user information.
'''
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
    AuthUser Model with all the basic properties.
    @Derived<AbstractUser>

    $property: dob | Date Of Birth of the user
    $property: phone_number | Phone Number of the user
'''
class AuthUser(AbstractUser):
    age = models.IntegerField(null=True, blank=False)
    phone_number = models.CharField(max_length=10, null=True, blank=False)

    def __str__(self):
        return self.username
