from django.urls import path, include, reverse_lazy
from .views import all_shoes

urlpatterns = [
    path('all_shoes/', all_shoes, name="all_shoes"),
]