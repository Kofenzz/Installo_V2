from django.urls import path

from category import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_view, name='category_view'),

]