from django.contrib import admin

from category.models import Category
from products.models import Products

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)