from django.shortcuts import get_object_or_404
from shop.models import Shoe


def cart_contents(request):
    """
    Display cart contents on any page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    #make quantity into dictionry of size and quantity
    for line_id, line_info in cart.items():
        product_id, size = line_id.split("-")
        product = get_object_or_404(Shoe, pk=product_id)
        quantity = line_info['quantity']
        total += quantity * product.price
        #total += info['quantity'] * product.price

        product_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'product': product, 'size':size})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}