from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class CartItem(models.Model):
    cart = models.ForeignKey(
        "Cart", on_delete=models.CASCADE, verbose_name='Cart', related_name='cart_items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='product')
    quantity = models.PositiveIntegerField('quantity')
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    @property
    def stock_count(self):
        return self.product.amount_left

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Customer', related_name="carts")
    items = models.ManyToManyField(CartItem, related_name='items')
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    ordered = models.BooleanField(default=False)
    
    @property
    def total_price(self):
        return sum([cartitem.product.price * cartitem.quantity for cartitem in self.cart_items.all()
                    if cartitem.cart_item_status == 'Available'])

    def __str__(self):
        return f'User = {self.user}; pk = {self.pk}'



# Each user should have cart
# When user registered create cart model with this user

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
