# Generated by Django 4.2.5 on 2023-09-20 13:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_cart_cartitems"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"verbose_name": "Cart", "verbose_name_plural": "Carts"},
        ),
        migrations.AlterModelOptions(
            name="cartitems",
            options={"verbose_name": "Cart-Item", "verbose_name_plural": "Cart-Items"},
        ),
    ]
