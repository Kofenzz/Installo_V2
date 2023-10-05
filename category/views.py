from django.core.paginator import Paginator
from django.shortcuts import render

from category.models import Category
from products.models import Products


# Create your views here.

def category_view(request, category_slug):

    category = Category.objects.get(slug=category_slug)
    products = Products.objects.filter(category=category).order_by('id')

    # to be implemented later the filters are


    # Configure Pagination

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)


    context = {
        'category': category,
        'products': products
    }

    return render(request,'category/category_detail.html',context)