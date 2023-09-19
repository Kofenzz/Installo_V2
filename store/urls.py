from django.urls import path

from store import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
]
