from django.db import models
from django.contrib.auth.models import User


# -------- Product Models----------->

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    product_description = models.TextField(
        max_length=255, blank=True, null=True)
    product_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.product_name

# -------- Cart Models ------------>


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()

# -------- ProductInCart ------------>


class ProductInCart(models.Model):
    class Meta:
        unique_together = (('cart', 'product'),)
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


# -------- Orders ------------>

class Order(models.Model):
    status_choices = (
        (1, 'Not Packed'),
        (2, 'Ready For shipment'),
        (3, 'Shipped'),
        (4, 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choices, default=1)
