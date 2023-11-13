from django.urls import path

from orders import views

urlpatterns = [
    path('order/', views.checkout, name='checkout'),
    path('order/thank-you', views.order_thank_you, name='order-thank-you'),
    path('profile/orders/', views.view_orders, name='view-orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_details'),
    path('orders/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
