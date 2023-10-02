from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    name = "custom_user"
    verbose_name = "Accounts Management"

    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import custom_user.signals