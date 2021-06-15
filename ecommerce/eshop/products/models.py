from django.db import models
from decimal import Decimal
from catalog.models import Catalog
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from datetime import datetime
from PIL import Image
from io import BytesIO
import os


class Product(models.Model):
    name = models.CharField(max_length=60, blank=False)
    descriptions = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.01'))], blank=False)
    raiting = models.FloatField(default=0.0)
    quantity = models.PositiveSmallIntegerField(blank=False)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/', null=False, default='products/nophoto.png')
    small_image = models.ImageField(
        upload_to='products/%Y/%m/%d/small/', null=True, editable=False)

    sku = models.CharField(max_length=20, blank=False, unique=True)
    categories = models.ManyToManyField(Catalog, verbose_name="Category")
    available = models.BooleanField(default=True, verbose_name="Available")

    def save(self, *args, **kwargs):
        image_size = (300, 300)
        self.make_small_image(size=image_size, dest_field=self.small_image)
        super(Product, self).save(*args, **kwargs)

    def make_small_image(self, size, dest_field):
        image = Image.open(self.image)
        if image.height > size[0] or image.width > size[1]:
            image.thumbnail(size, Image.ANTIALIAS)
            sm_img_name, sm_img_extension = os.path.splitext(self.image.name)
            sm_img_extension = sm_img_extension.lower()
            sm_img_filename = sm_img_name + '_thumb' + sm_img_extension

            if sm_img_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif sm_img_extension == '.png':
                FTYPE = 'PNG'

            temp_sm_img = BytesIO()
            image.save(temp_sm_img, FTYPE)
            temp_sm_img.seek(0)
            dest_field.save(sm_img_filename, ContentFile(
                temp_sm_img.read()), save=False)
            temp_sm_img.close()
        return True

    def __str__(self):
        return f"{self.pk}, {self.name}, {self.sku}"

    class Meta:
        ordering = ['name', '-price']


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True)

    def save(self, *args, **kwargs):
        super(ProductImage, self).save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.rating)
