from django.contrib import admin
from .models import Shoe, ProductImage, CustomerReview, Stock

admin.site.register(Shoe)
admin.site.register(Stock)
admin.site.register(ProductImage)
admin.site.register(CustomerReview)
