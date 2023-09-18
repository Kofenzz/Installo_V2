from django.urls import path

from products import views

urlpatterns = [
    path('produs/<str:slug>/<int:id>/',views.product_detail, name='product-detail'),
]