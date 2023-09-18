from django.shortcuts import render

from products.models import Products


def product_detail(request, slug, id):
    product = Products.objects.get(id=id)

    return render(request, 'products/product_detail.html', {'product': product})
