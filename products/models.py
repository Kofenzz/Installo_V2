from django.db import models

from category.models import Category


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=1000, null=False)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products/', null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'produs'
        verbose_name_plural = 'produse'

    def __str__(self):
        return f'{self.name} {self.price}'
