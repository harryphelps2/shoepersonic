from django.shortcuts import render

def checkout(request):
    """Make payment"""
    return render(request, 'checkout.html')