from django.shortcuts import render
from shop.models import Shoe
from django.contrib import auth, messages

def index(request):
    """Homepage view"""
    all_shoes = Shoe.objects.all()
    users = auth.models.User.objects.all()
    print(users)
    return render(request, 'index.html', {'all_shoes':all_shoes})

