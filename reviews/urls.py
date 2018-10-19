from django.urls import re_path, path, include, reverse_lazy
from .views import reviews

urlpatterns = [
    path('', reviews, name="reviews"),
]