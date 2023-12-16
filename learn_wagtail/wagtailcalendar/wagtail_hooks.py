from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import index


@hooks.register("register_admin_urls")
def register_calendar_url():
    return [
        path("calendar/", index, name="calendar"),
    ]


@hooks.register("register_admin_menu_item")
def register_calendar_menu_item():
    return MenuItem("Calendar", reverse("calendar"), icon_name="date")
