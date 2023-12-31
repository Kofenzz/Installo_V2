# Generated by Django 4.2.5 on 2023-10-18 10:05

from django.db import migrations


def populate_address_with_foreign_keys(apps, schema_editor):
    User = apps.get_model('custom_user', 'User')
    Address = apps.get_model('custom_user', 'Address')

    for user in User.objects.all():
        # Create an Address instance for each user and assign the foreign key
        address = Address.objects.create(user=user)
        try:
            address = Address.objects.get(user=user)
            address.save()
        except Address.DoesNotExist:
            pass

class Migration(migrations.Migration):
    dependencies = [
        ("custom_user", "0015_auto_20231018_1300"),
    ]

    operations = [
        migrations.RunPython(populate_address_with_foreign_keys)
    ]


# Generated by Django 4.2.5 on 2023-10-18 10:10


