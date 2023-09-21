import json

from django.http import JsonResponse
from django.shortcuts import render

from products.models import Products, Cart, CartItems


def product_detail(request, slug, id):
    product = Products.objects.get(id=id)

    return render(request, 'products/product_detail.html', {'product': product})


# Add to cart functionality only when logged in.
# This file works with the file static/js/scrips.js file
# Function addtoCart, getCookie

def cart(request):
    cart = None
    cart_items = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cart_items = cart.cart_items.all()

    context = {
        'cart': cart,
        'items': cart_items,
    }

    return render(request, 'products/cart.html', context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)  # from the model Cart
        cart_items, created = CartItems.objects.get_or_create(cart=cart, product=product)  # name of the product
        cart_items.quantity += 1  # start quantity
        cart_items.save()  # need to save to have the start quantity

        num_of_items = cart.num_of_items  # to update in realtime the cart, with some editind in static/js/scrpts.js

        print(cart_items)

    return JsonResponse(num_of_items, safe=False)


def update_cart_quantity(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    cart_id = data['cart_id']
    increase = data['increase']

    cart_item = CartItems.objects.filter(product_id=product_id, cart_id=cart_id).first()

    if cart_item is not None and cart_item.quantity >= 1:
        cart_item.quantity = cart_item.quantity + 1 if increase else cart_item.quantity - 1
        cart_item.save()
        # Return a dictionary as the JSON response
        response_data = {'message': 'Cart item updated successfully'}  # You can customize this message as needed
        return JsonResponse(response_data)
    elif cart_item.quantity == 0 or cart_item.quantity < 0:
        cart_item.quantity = 1
        cart_item.save()


    # If cart_item is not found, return an empty dictionary as the JSON response
    return JsonResponse({})
