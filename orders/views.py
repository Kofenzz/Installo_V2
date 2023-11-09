from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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

        return redirect('order-thank-you')

    context = {
        'cart': cart,
    }

    return render(request, 'order/checkout.html', context)
