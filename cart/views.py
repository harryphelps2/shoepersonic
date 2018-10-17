from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A view that renders the cart contents"""
    cart = request.session.get('cart', {})
    print(cart)
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity product to cart"""
    quantity = int(request.POST.get('quantity'))
    size = int(request.POST.get('size'))
    line_id = f"{id}-{size}"

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
    # in the form we get the new quantity and the id of the shoe
    quantity = int(request.POST.get('new_quantity'))
    cart = request.session.get('cart', {})
    # in the cart we get {'3-8': {'quantity': 3, 'size': 8}}
    line_id = f"{id}-{size}"
    print(line_id) 

    if quantity > 0:
        cart[line_id]["quantity"] = quantity
    else:
        cart.pop(line_id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
