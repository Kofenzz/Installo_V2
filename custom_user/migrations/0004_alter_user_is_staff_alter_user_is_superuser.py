# Generated by Django 4.2.5 on 2023-09-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "custom_user",
            "0003_user_created_at_user_updated_at_alter_user_is_staff_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
