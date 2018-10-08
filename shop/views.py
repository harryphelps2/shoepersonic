from django.shortcuts import render
from .models import Shoe

def all_shoes(request):
    """
    View to show all shoes.
    """
    all_shoes = Shoe.objects.all()
    return render(request, 'all_shoes.html', {'all_shoes':all_shoes})
