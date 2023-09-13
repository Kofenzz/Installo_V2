from datetime import datetime

from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models


class User(BaseUser):
    objects = BaseUserManager()
    phone_number = models.IntegerField(default=0)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    # is_company = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# class Address(models.Model):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#    #  recipient_name = models.CharField(max_length=50, null=False)
#    #  street_address1 = models.CharField(max_length=100, null=False)
#    #  street_address2 = models.CharField(max_length=100, null=True)
#    # # city = models.CharField(choices= #, max_length=100 )
#    #  postal_code = models.IntegerField(default=0)
#    #  country = models.CharField(choices= ,max_length=100)
#    #  state = models.CharField(choices= , max_length==100)
#





