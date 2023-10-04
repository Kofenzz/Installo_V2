# from carts.models import Cart, CartItem
import random
import warnings
from datetime import datetime, timedelta

from django.db.models import Q

from category.models import Category
from products.forms import ProductSearchForm
from products.models import Products, Cart
from store.models import Carousels


def get_category(request):
    return {"categories": Category.objects.all()}


def get_product(request):
    return {"products": Products.objects.all()}


def random_products(request):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    products = Products.objects.filter(Q(created_at__range=(thirty_days_ago, datetime.now())))
    random_sample = random.sample(list(products), 4)  # Change 3 to the desired number of random products
    return {'random_products': random_sample}

def get_new_products(request):
    warnings.filterwarnings('ignore', category=RuntimeWarning, module='django.db.models.fields')

    products = Products.objects.all()
    sample = random.sample(list(products), 4)
    return {'new_products' : sample}

def best_seller(request):
    pass


def get_carousel(request):
    carousels = Carousels.objects.order_by('order')[:3]
    return {'carousels': carousels}


def get_num_of_items(request):
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    return {'cart': cart}


def get_search_context(request):
    search = ProductSearchForm()
    return {'search': search}
