# Generated by Django 4.2.5 on 2023-10-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("custom_user", "0013_auto_20231018_1259"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="address_name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="recipient_name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="street_address1",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
