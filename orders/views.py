from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from orders.models import OrderItem, Order
from products.models import Cart


@login_required
def checkout(request):
    user = request.user

    try:
        cart = Cart.objects.get(user=user, completed=False)
    except Cart.DoesNotExist:
        return redirect('cart')

    if request.method == 'POST':
        order = Order(user=user)
        order.save()

        for cart_item in cart.cart_items.all():
            order_item = OrderItem(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price * cart_item.quantity,
            )
            order_item.save()

        cart.completed = True
        cart.save()

        request.session['order_number'] = str(order.order_number)
        return redirect('order-thank-you')

    context = {
        'cart': cart,
        'items': cart.cart_items.all()
    }

    return render(request, 'order/checkout.html', context)


@login_required
def order_thank_you(request):
    user = request.user

    try:
        # Get the most recent order for the logged-in user
        latest_order = Order.objects.filter(user=user).latest('created_at')
    except Order.DoesNotExist:
        # Handle cases where no order is found
        raise Http404("No Order Found")

    context = {
        'first_name': user.first_name,
        'order_number': latest_order.order_number
    }

    return render(request, 'order/thank_you.html', context)


@login_required
def view_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')

    context = {'orders': orders}

    return render(request, 'custom_user/profile_menu/view_orders.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)

    for item in order_items:
        item.total_price = item.quantity * item.product.price

    context = {
        'order':order,
        'order_items':order_items
    }

    return render(request,'order/order_details.html',context)


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'Pending':
        order.status = 'Cancelled'  # Or whatever your cancelled status is
        order.save()

    # Redirect back to the order details page or another appropriate page
    return HttpResponseRedirect(reverse('order_details', args=[order.id]))