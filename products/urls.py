from django.urls import path

from products import views

urlpatterns = [
    path('produs/<str:slug>/<int:id>/', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('search/add-to-cart/', views.add_to_cart, name='search_add_to_cart'),
    path('produs/<str:slug>/<int:id>/add-to-cart/', views.add_to_cart, name='product_detail_add_to_cart'),
    path('update-cart-quantity/', views.update_cart_quantity, name='update-cart-quantity'),
    path('delete-cart-item/<int:product_id>/', views.delete_cart_item, name='delete-cart-item'),
    path('search/', views.product_search, name='product_search'),
]
