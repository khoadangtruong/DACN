from order.models import ShopCart
from django.contrib import admin

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

admin.site.register(ShopCart, ShopCartAdmin)
