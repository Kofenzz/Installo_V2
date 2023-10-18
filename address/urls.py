from django.urls import path

from address import views

urlpatterns = [
    path('profile/address/edit/', views.edit_address, name='edit_address'),
    path('profile/address/', views.AddressListView.as_view(), name='view_address')
]
