from django.db.models.signals import post_save
from django.dispatch import receiver

from custom_user.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        # sending the names aswell
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.save()
