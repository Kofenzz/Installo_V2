from django.db import models

from custom_user.models import User


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.county}'

#
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    address_name = models.CharField(max_length=50, null=True)
    recipient_name = models.CharField(max_length=50, null=True)
    street_address1 = models.CharField(max_length=100, null=True)
    street_address2 = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    postal_code = models.IntegerField(default=0, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
