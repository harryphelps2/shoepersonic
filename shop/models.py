from django.db import models

SHOE_TYPE_CHOICES = [
    ('flats', 'FLATS'),
    ('track spikes', 'TRACK SPIKES'),
    ('cross country spikes', 'CROSS COUNTRY SPIKES'),
    ('pluggers', 'PLUGGERS')
]

class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    description = models.TextField()
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPE_CHOICES)
    weight = models.IntegerField()
    drop_height = models.IntegerField()

    def __str__(self):
        return self.name
    
    

"""

model for stock:
id:
shoe(id):
size:
gender:
stock level:

model for shoe images:
shoe(id):
image:

"""