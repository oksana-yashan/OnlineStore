# Generated by Django 3.1.4 on 2021-04-21 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210325_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]