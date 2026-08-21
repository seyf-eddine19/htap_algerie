from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView
from django.utils.translation import gettext_lazy as _
from .models import Member
from .forms import ContactMessageForm

from articles.models import Article


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = (
            Article.objects.filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related("translations")
            .order_by("-published_at", "-created_at")[:3]
        )
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.filter(is_active=True).only('id', 'name', 'name_ar', 'role_ar', 'role_en', 'role_fr', 'photo', 'bio')
        return context


class HTAPView(TemplateView):
    template_name = "core/htap.html"


class HelpView(TemplateView):
    template_name = "core/help.html"


class MembershipView(TemplateView):
    template_name = "core/membership.html"


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactMessageForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("Your message has been sent successfully."))
        return redirect("core:contact")

    def form_invalid(self, form):
        messages.error(self.request, _("Please correct the errors below."))
        return super().form_invalid(form)