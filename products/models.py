import uuid

from autoslug import AutoSlugField
from django.db import models

from category.models import Category
from custom_user.models import User


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(max_length=2000, null=False)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'produs'
        verbose_name_plural = 'produse'

    def __str__(self):
        return f'{self.name} {self.price}'


# Cart Model

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return str(self.id)

    # Total Price of the Cart
    @property
    def total_price(self):
        cart_items = self.cart_items.all()  # cart_items vine de la linia 52
        total = sum([item.price for item in cart_items])
        return total

    # Get the quantity of the cart items to have them displayed in navbar
    # This will only show in cart page
    @property
    def num_of_items(self):
        cart_items = self.cart_items.all()  # cart_items vine de la linia 52
        quantity = sum([item.quantity for item in cart_items])
        return quantity


class CartItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Cart-Item'
        verbose_name_plural = 'Cart-Items'

    def __str__(self):
        return self.product.name

    # Make the total price of the X number of the same items
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
