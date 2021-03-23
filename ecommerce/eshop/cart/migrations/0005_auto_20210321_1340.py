# Generated by Django 3.1.4 on 2021-03-21 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
        ('cart', '0004_auto_20210321_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product'),
        ),
    ]