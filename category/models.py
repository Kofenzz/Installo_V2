from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=1000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True, related_name='sub_category')

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categorii'

    def __str__(self):
        return self.name

