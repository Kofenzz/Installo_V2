import json

from django.db import models

from custom_user.models import User


# Create your models here.
class Address(models.Model):
    CITY_CHOICES = []

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    address_name = models.CharField(max_length=50, null=True)
    recipient_name = models.CharField(max_length=50, null=True)
    street_address1 = models.CharField(max_length=100, null=True)
    street_address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(choices=CITY_CHOICES, max_length=100)
    postal_code = models.IntegerField(default=0, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


with open('static/data/cities.json') as json_file:
    cities_data = json.load(json_file)

CITY_CHOICES = [(city['city'], city['city']) for city in cities_data]
Address.CITY_CHOICES = CITY_CHOICES
