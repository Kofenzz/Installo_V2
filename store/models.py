from django.contrib import admin
from django.db import models

# Create your models here.

class Carousels(models.Model):
    image = models.ImageField(upload_to='carousels/%y/%m/', null=True)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=50, null=True)
    order = models.IntegerField(default=0, help_text="Order in which the carousel appears")
    link = models.URLField(max_length=200, blank=True,null=True)

    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'



    def __str__(self):
        return self.title

class CarouselsAdmin(admin.ModelAdmin):

    list_display = ('title','order', 'link')