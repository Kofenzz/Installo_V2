from django.db import models

# Create your models here.

class Carousels(models.Model):
    image = models.ImageField(upload_to='carousels/%y/%m/', null=True)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.title