from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    points = models.IntegerField(blank=False, null=False, default=0)
    id_proof_key = models.CharField(max_length=20, blank=False, null=True)

    # Address Attributes
    street = models.CharField(max_length=30, blank=False, null=True)
    city = models.CharField(max_length=30, blank=False, null=True)
    state = models.CharField(max_length=30, blank=False, null=True)
    zip_code = models.CharField(max_length=6, blank=False, null=True)

    def __str__(self):
        return self.user.username
 