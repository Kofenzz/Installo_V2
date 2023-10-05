from django.urls import path

from category import views
from products.views import add_to_cart

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_view, name='category_view'),
    path('category/<slug:category_slug>/add-to-cart/', add_to_cart, name= 'category_add_to_cart')

]