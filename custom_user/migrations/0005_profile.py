# Generated by Django 4.2.5 on 2023-10-02 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("custom_user", "0004_alter_user_is_staff_alter_user_is_superuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("phone_number", models.CharField(max_length=20)),
                ("address_1", models.CharField(max_length=200)),
                ("address_2", models.CharField(max_length=200)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("Individual", "Individual"), ("Company", "Company")],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
