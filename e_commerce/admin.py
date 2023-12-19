from django.contrib import admin
from .models import Product, Cart, ProductInCart, Order

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'price']


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'user',]


admin.site.register(Cart, CartAdmin)


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['product_in_cart_id', 'cart',]


admin.site.register(ProductInCart, ProductInCartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status',]


admin.site.register(Order, OrderAdmin)
