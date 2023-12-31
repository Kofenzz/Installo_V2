import json

from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    objects = BaseUserManager()
    phone_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



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
