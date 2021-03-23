from django.db import models
from datetime import datetime

from user.models import UserProfile
from products.models import Product


class Order(models.Model):
    ORDERS_STATUS = [
        ('Processed', 'Processed'),
        ('On_road', 'On road'),
        ('Delivery', 'Delivery'),
        ('Received', 'Received')
    ]
    SHIPMENT = [
        ('Courier_delivery', 'Courier delivery'),
        ('Mail_delivery', 'Mail delivery'),
        ('Pickup', 'Pickup')
    ]

    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_timedate = models.DateTimeField(default=datetime.now)
    content = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_type = models.CharField(max_length=20, choices=SHIPMENT)
    status = models.CharField(max_length=20, choices=ORDERS_STATUS)
    is_active = models.BooleanField(default=True, verbose_name='Active?')

    def __str__(self):
        return f' {self.customer}, {self.order_timedate}, {self.content}, {self.price}, {self.shipment_type},' \
               f' {self.status}, {self.is_active} '
