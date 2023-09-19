from django.contrib import admin

from store.models import Carousels

# Register your models here.

from store.models import Carousels, CarouselsAdmin

admin.site.register(Carousels,CarouselsAdmin)

