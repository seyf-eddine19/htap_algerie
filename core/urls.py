from django.urls import path
from .views import HomeView, AboutView, HTAPView, HelpView, MembershipView, ContactView

app_name = "core"

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("htap/", HTAPView.as_view(), name="htap"),
    path("help/", HelpView.as_view(), name="help"),
    path("membership/", MembershipView.as_view(), name="membership"),
    path("contact/", ContactView.as_view(), name="contact"),
)