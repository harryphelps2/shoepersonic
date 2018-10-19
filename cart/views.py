from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A view that renders the cart contents"""
    cart = request.session.get('cart', {})
    print(cart)
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity product to cart"""
    # build in check that stops them submitting if they don't select size
    quantity = int(request.POST.get('quantity'))
    size = int(request.POST.get('size'))
    line_id = "{0}-{1}".format(id, size)

    cart = request.session.get('cart', {})

    # if the line id not in the basket
    # add to basket with quanitityt of 0
    if line_id not in cart:
        cart[line_id] = {
            'quantity': 0,
            'size': size
        }

    cart[line_id]["quantity"] += quantity

    request.session['cart'] = cart
    print(cart)
    # redirect to spike store?
    return redirect(reverse('view_cart'))

def adjust_cart(request, id, size):
    """Adjust quantity of the product to the specified amount"""
    quantity = int(request.POST.get('new_quantity'))
    cart = request.session.get('cart', {})
    line_id = f"{id}-{size}"
    print(line_id) 

    if quantity > 0:
        cart[line_id]["quantity"] = quantity
    else:
        cart.pop(line_id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
