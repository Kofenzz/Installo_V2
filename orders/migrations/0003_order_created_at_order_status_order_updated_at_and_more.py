# Generated by Django 4.2.5 on 2023-11-08 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0008_alter_cart_options_alter_cartitems_options"),
        ("orders", "0002_remove_order_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
        ),
    ]
