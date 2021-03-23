from django.db import models
from decimal import Decimal
from catalog.models import Catalog
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=60, blank=False)
    descriptions = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.01'))], blank=False)
    raiting = models.FloatField(default=0.0)
    quantity = models.PositiveSmallIntegerField(blank=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d/',null=False, default='products/nophoto.png')

    sku = models.CharField(max_length=10, blank=False, unique=True)
    categories = models.ManyToManyField(Catalog, verbose_name="Category")
    available = models.BooleanField(default=True, verbose_name="Available")

    def __str__(self):
        return f"{self.pk}, {self.name}, {self.sku}"

    class Meta:
        ordering = ['name', '-price']


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='mediafiles')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True)

    def save(self, *args, **kwargs):
        super(ProductImage, self).save(*args, **kwargs)
