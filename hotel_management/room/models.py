from django.db import models

# Create your models here.

ROOM_TYPE_CHOICES = [('BUD', 'Budget'),('ECO', 'Economy'), ('DEL', 'Delux'), ('PRI', 'Prime'), ('SUI', 'Suit')]

ROOM_FLOOR_CHOICES = [(0, 'Ground'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')]

class Room(models.Model):
    type = models.CharField(max_length=3, blank=False, null=True, choices=ROOM_TYPE_CHOICES)
    floor = models.IntegerField(blank=False, null=True, choices=ROOM_FLOOR_CHOICES)
    room_no = models.CharField(max_length=3, blank=False, null=True)
    description = models.TextField()

    def __str__(self):
        return self.type + ' ' + str(self.room_no)
