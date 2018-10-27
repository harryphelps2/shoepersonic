from django.contrib import admin
from .models import Shoe, StockLevel, ProductImage, CustomerReview

admin.site.register(Shoe)
admin.site.register(StockLevel)
admin.site.register(ProductImage)
admin.site.register(CustomerReview)
