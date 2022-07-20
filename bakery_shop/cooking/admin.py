from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_product', 'cost')
    search_fields = ('name', 'cost')


class TypeProductAdmin(admin.ModelAdmin):
    list_display = ('type_product', 'unit')
    search_fields = ('type_product', 'unit')


class ShopsAdmin(admin.ModelAdmin):
    list_display = ('name_shop', 'address_shop')
    search_fields = ('name_shop',)


class CountProductsInShopAdmin(admin.ModelAdmin):
    list_display = ('product', 'count', 'shop')
    search_fields = ('product', 'count', 'shop')


admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.TypeProducts, TypeProductAdmin)
admin.site.register(models.Shops, ShopsAdmin)
admin.site.register(models.CountProductsInShop, CountProductsInShopAdmin)

# Register your models here.
