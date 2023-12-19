from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from e_commerce.models import Cart


class CartInline(admin.TabularInline):
    model = Cart


class DealInline(admin.TabularInline):
    model = Cart.user.through


# --------------  customized User Models (-- Not working -- ) ------------------>


class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'get_cart', 'is_staff', 'is_active')
    list_filter = ('username', 'is_staff', 'is_active')

    inlines = [
            CartInline, DealInline
    ]

    def get_cart(self, obj):
        return obj.cart

    search_fields = ('username')
    ordering = ('username')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

