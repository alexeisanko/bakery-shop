from django.contrib import admin
from . import models


class BakeryUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'id_loyalty')
    search_fields = ('username',)


class LoyaltyCardAdmin(admin.ModelAdmin):
    list_display = ('level_loyalty', 'discount', )
    search_fields = ('level_loyalty', 'discount',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('numbers_order', 'date_order', 'count_product')


admin.site.register(models.BakeryUser, BakeryUserAdmin)
admin.site.register(models.LoyaltyCard, LoyaltyCardAdmin)
admin.site.register(models.Order)


# Register your models here.
