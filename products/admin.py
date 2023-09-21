# Register your models here.
from django.contrib import admin

from products.models import Products, Cart, CartItems

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItems)