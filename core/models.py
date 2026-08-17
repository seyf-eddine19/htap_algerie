from django.db import models
from django.utils.translation import gettext_lazy as _, get_language


# class AssociationInfo(models.Model):
#     name = models.CharField(_("name"), max_length=200, default="HTAP Algérie")
#     full_name = models.CharField(_("full name"), max_length=300, blank=True)
#     description = models.TextField(_("description"), blank=True)
#     history = models.TextField(_("history"), blank=True)
#     mission = models.TextField(_("mission"), blank=True)
#     objectives = models.TextField(_("objectives"), blank=True)
#     logo = models.ImageField(_("logo"), upload_to="association/", blank=True, null=True)
#     address = models.TextField(_("address"), blank=True)
#     phone = models.CharField(_("phone"), max_length=50, blank=True)
#     email = models.EmailField(_("email"), blank=True)
#     facebook_url = models.URLField(_("Facebook"), blank=True)
#     instagram_url = models.URLField(_("Instagram"), blank=True)
#     youtube_url = models.URLField(_("YouTube"), blank=True)
#     map_url = models.URLField(_("map URL"), blank=True)
#     updated_at = models.DateTimeField(_("updated at"), auto_now=True)

#     class Meta:
#         verbose_name = _("Association information")
#         verbose_name_plural = _("Association information")

#     def __str__(self):
#         return self.name


# class Statistic(models.Model):
#     title = models.CharField(_("title"), max_length=100)
#     value = models.CharField(_("value"), max_length=50)
#     description = models.CharField(_("description"), max_length=200, blank=True)
#     icon = models.CharField(_("icon"), max_length=50, blank=True, help_text=_("Icon name used by the frontend."))
#     order = models.PositiveIntegerField(_("order"), default=0)
#     is_active = models.BooleanField(_("active"), default=True)

#     class Meta:
#         ordering = ["order"]
#         verbose_name = _("Statistic")
#         verbose_name_plural = _("Statistics")

#     def __str__(self):
#         return f"{self.title} - {self.value}"

class Member(models.Model):
    name = models.CharField(_("Name (Latin characters)"), max_length=150)
    name_ar = models.CharField(_("Name (Arabic)"), max_length=150, blank=True)
    role_ar = models.CharField(_("Role (Arabic)"), max_length=150, blank=True)
    role_en = models.CharField(_("Role (English)"), max_length=150, blank=True)
    role_fr = models.CharField(_("Role (French)"), max_length=150)
    photo = models.ImageField(_("Photo"), upload_to="members/", blank=True, null=True)
    bio = models.TextField(_("Bio"), blank=True)
    order = models.PositiveIntegerField(_("order"), default=0)
    is_active = models.BooleanField(_("active"), default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    @property
    def display_name(self):
        lang = get_language()
        if lang == "ar" and self.name_ar:
            return self.name_ar
        return self.name or self.name_ar

    @property
    def display_role(self):
        lang = get_language()
        if lang == "ar":
            return self.role_ar or self.role_fr
        if lang == "fr":
            return self.role_fr or self.role_en
        return self.role_en or self.role_fr or self.role_en
    
    def __str__(self):
        return f"{self.name} - {self.role}"


class ContactMessage(models.Model):
    class Status(models.TextChoices):
        NEW = "new", _("New")
        READ = "read", _("Read")
        REPLIED = "replied", _("Replied")
        ARCHIVED = "archived", _("Archived")

    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100, blank=True)
    email = models.EmailField(_("email"))

    phone = models.CharField(_("phone"), max_length=50, blank=True)
    subject = models.CharField(_("subject"), max_length=200)
    message = models.TextField(_("message"))

    status = models.CharField(_("status"), max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Contact message")
        verbose_name_plural = _("Contact messages")

    def __str__(self):
        return f"{self.subject} - {self.email}"