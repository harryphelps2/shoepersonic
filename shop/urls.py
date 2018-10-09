from django.urls import path, include, reverse_lazy
from .views import all_shoes, track_spikes, xc_spikes, pluggers, flats

urlpatterns = [
    path('all_shoes/', all_shoes, name="all_shoes"),
    path('flats/', flats, name="flats"), 
    path('xc_spikes/', xc_spikes, name="xc_spikes"),
    path('pluggers/', pluggers, name="pluggers"),
    path('track_spikes/', track_spikes, name="track_spikes"),
]