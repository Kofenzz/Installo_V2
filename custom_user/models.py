import json

from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    objects = BaseUserManager()
    phone_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Address(models.Model):
#     # CITY_CHOICES = []
#     #
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     #
#     # address_name = models.CharField(max_length=50, null=True)
#     # recipient_name = models.CharField(max_length=50, null=True)
#     # street_address1 = models.CharField(max_length=100, null=True)
#     # street_address2 = models.CharField(max_length=100, null=True)
#     # city = models.CharField(choices=CITY_CHOICES, max_length=100)
#     # postal_code = models.IntegerField(default=0, null=True)
#     #
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)
#     pass


# with open('static/data/cities.json') as json_file:
#     cities_data = json.load(json_file)
#
# CITY_CHOICES = [(city['city'], city['city']) for city in cities_data]
# Address.CITY_CHOICES = CITY_CHOICES


class Profile(models.Model):
    TYPE_CHOICES = (
        ('Individual', 'Individual'),
        ('Company', 'Company'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    user_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

# DE IMPLEMENTAT
# class ContactUs(models.Model):
#
#     full_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     phone = models.CharField(max_length=20)
#     subject = models.CharField(max_length=100)
#     message = models.TextField()
#
#     class Meta:
#         verbose_name = 'Contact'
#         verbose_name_plural = 'Contact'
#
#     def __str__(self):
#         return self.full_name
