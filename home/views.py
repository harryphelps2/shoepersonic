from django.shortcuts import render
from shop.models import Shoe

def index(request):
    """Homepage view"""
    all_shoes = Shoe.objects.all()
    return render(request, 'index.html', {'all_shoes':all_shoes})

