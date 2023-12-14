from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "learn_wagtail.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import learn_wagtail.users.signals  # noqa: F401
        except ImportError:
            pass
