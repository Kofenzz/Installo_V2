from django.urls import path

from custom_user import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.UserLoginPageView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),

]
