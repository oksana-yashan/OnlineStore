# Generated by Django 2.2 on 2021-03-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/nophoto.png', upload_to='products/%Y/%m/%d/'),
        ),
    ]
