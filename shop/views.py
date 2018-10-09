from django.shortcuts import render
from .models import Shoe

def all_shoes(request):
    """
    View to show all shoes.
    """
    all_shoes = Shoe.objects.all()
    return render(request, 'all_shoes.html', {'all_shoes':all_shoes})

def track_spikes(request):
    """
    View track spikes.
    """
    track_spikes = Shoe.objects.filter(shoe_type="track spikes")
    return render(request, 'track_spikes.html', {'track_spikes':track_spikes})

def xc_spikes(request):
    """
    View xc spikes.
    """
    xc_spikes = Shoe.objects.filter(shoe_type="cross country spikes")
    return render(request, 'xc_spikes.html', {'xc_spikes':xc_spikes})

def pluggers(request):
    """
    View pluggers.
    """
    pluggers = Shoe.objects.filter(shoe_type="pluggers")
    return render(request, 'pluggers.html', {'pluggers':pluggers})


def flats(request):
    """
    View flats.
    """
    flats = Shoe.objects.filter(shoe_type="flats")
    return render(request, 'flats.html', {'flats':flats})