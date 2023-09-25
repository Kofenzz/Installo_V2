import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from products.forms import ProductSearchForm
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


def add_to_cart(request,slug,id):
    data = json.loads(request.body)
    product_id = data['id']
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)  # from the model Cart
        cart_items, created = CartItems.objects.get_or_create(cart=cart, product=product)  # name of the product
        cart_items.quantity += 1  # start quantity
        cart_items.save()  # need to save to have the start quantity

        num_of_items = cart.num_of_items  # to update in realtime the cart, with some editind in static/js/scrpts.js

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


def delete_cart_item(request, product_id):
    # Get the product to be deleted or return a 404 response if not found
    product = get_object_or_404(Products, id=product_id)

    # Get the user's cart (assuming the user is authenticated)
    cart = Cart.objects.get(user=request.user, completed=False)

    try:
        # Attempt to get the cart item corresponding to the product
        cart_item = CartItems.objects.get(cart=cart, product=product)

        # Delete the cart item
        cart_item.delete()

        # Optionally, you can update the cart total or perform any other necessary actions

        # Return a JSON response to indicate success
        response_data = {'message': 'Product removed from cart'}

        # Add a flag to indicate that the page should be reloaded
        response_data['reload_page'] = True

        return redirect('cart')
    except CartItems.DoesNotExist:
        # If the cart item does not exist, return an error message
        response_data = {'message': 'Product not found in cart'}
        return JsonResponse(response_data, status=404)


def product_search(request):

    # Initialize an empty list for search reulsts
    search_results = []

    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search')

            if search_query:
                search_results = Products.objects.filter (name__icontains=search_query)

    return render(request, 'products/search.html', {'search_results': search_results, 'form': form})


# @login_required()
# def search(request):
#     get_value = request.GET.get('filter')
#     if get_value:
#         students = Student.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
#     else:
#         students = Student.objects.all()
#
#     return render(request, 'student/list_of_students.html', {'all_students': students})
