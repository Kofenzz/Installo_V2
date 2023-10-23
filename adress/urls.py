from django.urls import path

from adress import views

urlpatterns = [
    path('profile/address/edit/<int:pk>', views.edit_address, name='edit_address'),
    path('profile/address/', views.AddressListView.as_view(), name='view_address'),
    path('profile/address/add/',views.AddressCreateView.as_view(), name='add_address'),
    path('profile/address/delete/<int:pk>',views.AddressDeleteView.as_view(), name='delete_address'),
]
