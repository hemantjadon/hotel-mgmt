from django.db import models
from room.models import Room
from customer.models import Customer

# Create your models here.

RATING_CHOICES = [(5, 'Very Satified'), (4, 'SatisFied'), (3, 'Okayish'), (2, 'Dissatisfied'), (1, 'Very Dissatisfied')]

class Booking(models.Model):
    check_in_date = models.DateField(blank=False, null=True)
    check_out_date = models.DateField(blank=False, null=True)
    room = models.ForeignKey(Room, blank=False, null=True)
    customer = models.ForeignKey(Customer, blank=False, null=True)
    price = models.IntegerField(blank=False, null=True)
    customer_points = models.IntegerField(default=0)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return 'Booking ' + str(self.pk)
