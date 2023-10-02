from django.db import migrations
from custom_user.models import Profile  # Import your Profile model
from custom_user.models import User  # Import your custom User model

def populate_profiles(apps, schema_editor):
    User1 = apps.get_model('custom_user', 'User')
    Profile1 = apps.get_model('custom_user', 'Profile')

    for user in User1.objects.all():
        try:
            profile = Profile1.objects.get(user=user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()
        except Profile1.DoesNotExist:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0008_auto_20231002_1311"),
    ]

    operations = [
        migrations.RunPython(populate_profiles),
    ]
