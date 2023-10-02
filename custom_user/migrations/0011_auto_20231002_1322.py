from django.db import migrations

def populate_profiles(apps, schema_editor):
    User = apps.get_model('custom_user', 'User')
    Profile = apps.get_model('custom_user', 'Profile')

    for user in User.objects.all():
        try:
            profile, created = Profile.objects.get_or_create(user=user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()
        except Profile.DoesNotExist:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0010_auto_20231002_1321"),  # Replace with the appropriate previous migration
    ]

    operations = [
        migrations.RunPython(populate_profiles),
    ]
