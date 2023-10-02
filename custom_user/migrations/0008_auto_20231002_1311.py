from django.db import migrations
from custom_user.models import Profile  # Import your Profile model
from custom_user.models import User  # Import your custom User model

def populate_profiles(apps, schema_editor):
    User = apps.get_model('custom_user', 'User')
    Profile = apps.get_model('custom_user', 'Profile')

    for user in User.objects.all():
        try:
            profile = Profile.objects.get(user=user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()
        except Profile.DoesNotExist:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0007_auto_20231002_1310"),
    ]

    operations = [
        migrations.RunPython(populate_profiles),
    ]
