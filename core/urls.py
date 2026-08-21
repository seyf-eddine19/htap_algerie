from django.urls import path
from django.views.decorators.cache import cache_page
from .views import HomeView, AboutView, HTAPView, HelpView, MembershipView, ContactView
app_name = "core"

urlpatterns = (
    path("", cache_page(60 * 15)(HomeView.as_view()), name="home"),
    path("about/", cache_page(60 * 15)(AboutView.as_view()), name="about"),
    path("htap/", cache_page(60 * 15)(HTAPView.as_view()), name="htap"),
    path("help/", cache_page(60 * 15)(HelpView.as_view()), name="help"),
    path("membership/", cache_page(60 * 15)(MembershipView.as_view()), name="membership"),
    path("contact/", cache_page(60 * 15)(ContactView.as_view()), name="contact"),
)