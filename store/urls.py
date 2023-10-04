from django.urls import path

from store import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('about-us/',views.about_us, name='about-us'),
    path('terms-and-conditions/', views.terms, name='terms-and-conditions'),
]
