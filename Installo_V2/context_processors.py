from category.models import Category
from products.models import Products


def get_category(request):
    return {"categories" : Category.objects.all()}

def get_product(request):
    return {"products": Products.objects.all()}

