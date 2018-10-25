from django.shortcuts import render
from .models import Shoe, StockLevel

def all_shoes(request):
    """
    View to show all shoes.
    """
    all_shoes = Shoe.objects.all()
    return render(request, 'all_shoes.html', {'all_shoes':all_shoes})

def shoes_for_him(request):
    """
    View track spikes.
    """
    track_spikes = Shoe.objects.filter(shoe_type="track spikes")
    return render(request, 'track_spikes.html', {'track_spikes':track_spikes})

def shoes_for_her(request):
    """
    View xc spikes.
    """
    xc_spikes = Shoe.objects.filter(shoe_type="cross country spikes")
    return render(request, 'xc_spikes.html', {'xc_spikes':xc_spikes})

def shoe_detail(request, shoe_id):
    """
    View to show detailed information about shoe and add to cart
    """
    shoe = Shoe.objects.get(pk=shoe_id)
    stock_level = StockLevel.objects.filter(shoe_model = shoe_id)
    return render(request, 'shoe_detail.html', {'shoe':shoe, 'stock_level':stock_level})
