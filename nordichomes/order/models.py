from django.db import models
from django.contrib.auth.models import User

from product.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (ORDERED, 'Shipped'),
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def get_total(self):
        return sum(item.price * item.quantity for item in self.items.all())

    def get_display_total(self):
        return f'$ {self.get_total()}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return f'$ {self.price}'