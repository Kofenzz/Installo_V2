# Generated by Django 4.2.5 on 2023-09-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_alter_products_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="description",
            field=models.TextField(max_length=2000),
        ),
    ]
