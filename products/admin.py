from django.contrib import admin
from .models import Products,Offer

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image_url')


admin.site.register(Products,ProductsAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer,OfferAdmin)