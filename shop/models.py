from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

SHOE_TYPE_CHOICES = [
    ('flats', 'FLATS'),
    ('track spikes', 'TRACK_SPIKES'),
    ('cross country spikes', 'CROSS_COUNTRY_SPIKES'),
    ('pluggers', 'PLUGGERS')
]

SHOE_SIZE_CHOICES = [
    ('6','6')
]

class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    strapline = models.TextField()
    description = models.TextField()
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPE_CHOICES)
    weight = models.IntegerField()
    drop_height = models.IntegerField()
    price = models.IntegerField()
    primary_image = models.ImageField()

    def __str__(self):
        return self.name
    
    
class StockLevel(models.Model):
    shoe_model = models.ForeignKey("Shoe", on_delete=models.CASCADE, null=True)
    size = models.IntegerField(default=10,
        validators=[MaxValueValidator(15), MinValueValidator(1)], null=True)
    stock = models.IntegerField(default=10, null=True)

    def __str__(self):
        stock_entry = "{0} size {1} has {2} left".format(self.shoe_model, self.size, self.stock)
        return stock_entry
    