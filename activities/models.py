# activities/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Language(models.TextChoices):
    ARABIC = "ar", _("Arabic")
    ENGLISH = "en", _("English")
    FRENCH = "fr", _("French")


class ActivityType(models.TextChoices):
    EVENT = "event", _("Event")
    INTERVIEW = "interview", _("Interview")
    CAMPAIGN = "campaign", _("Campaign")
    MEETING = "meeting", _("Meeting")
    CONFERENCE = "conference", _("Conference")
    OTHER = "other", _("Other")


class Activity(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")

    slug = models.SlugField(_("slug"), max_length=280, unique=True, blank=True)
    activity_type = models.CharField(_("activity type"), max_length=30, choices=ActivityType.choices, default=ActivityType.EVENT)
    status = models.CharField(_("status"), max_length=20, choices=Status.choices, default=Status.DRAFT)
    featured_image = models.ImageField(_("featured image"), upload_to="activities/%Y/%m/", blank=True, null=True)
    location = models.CharField(_("location"), max_length=250, blank=True)
    start_date = models.DateTimeField(_("start date"), null=True, blank=True)
    end_date = models.DateTimeField(_("end date"), null=True, blank=True)
    is_featured = models.BooleanField(_("featured"), default=False)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        ordering = ["-start_date", "-created_at"]
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")

    def __str__(self):
        translation = self.translations.first()
        return translation.title if translation else f"Activity #{self.pk}"

    def get_absolute_url(self):
        return reverse("activities:detail", kwargs={"slug": self.slug})

class ActivityTranslation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="translations", verbose_name=_("activity"))
    language = models.CharField(_("language"), max_length=2, choices=Language.choices)
    title = models.CharField(_("title"), max_length=250)
    excerpt = models.TextField(_("excerpt"), blank=True)
    meta_title = models.CharField(_("meta title"), max_length=250, blank=True)
    meta_description = models.CharField(_("meta description"), max_length=300, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["activity", "language"], name="unique_activity_language")
        ]
        verbose_name = _("Activity translation")
        verbose_name_plural = _("Activity translations")

    def __str__(self):
        return f"{self.title} ({self.language})"


class ActivityBlock(models.Model):

    class BlockType(models.TextChoices):
        HEADING = "heading", _("Heading")
        PARAGRAPH = "paragraph", _("Paragraph")
        IMAGE = "image", _("Image")
        QUOTE = "quote", _("Quote")

    translation = models.ForeignKey(ActivityTranslation, on_delete=models.CASCADE, related_name="blocks", verbose_name=_("translation"))
    block_type = models.CharField(_("block type"), max_length=20, choices=BlockType.choices)
    order = models.PositiveIntegerField(_("order"), default=0)
    title = models.CharField(_("title"), max_length=250, blank=True)
    text = models.TextField(_("text"), blank=True)
    image = models.ImageField(_("image"), upload_to="activities/blocks/%Y/%m/", blank=True, null=True)
    image_caption = models.CharField(_("image caption"), max_length=250, blank=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = _("Content block")
        verbose_name_plural = _("Content blocks")

    def __str__(self):
        return f"{self.translation.title} - {self.get_block_type_display()}"


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="gallery", verbose_name=_("activity"))
    image = models.ImageField(_("image"), upload_to="activities/gallery/%Y/%m/")
    caption = models.CharField(_("caption"), max_length=250, blank=True)
    order = models.PositiveIntegerField(_("order"), default=0)
    
    class Meta:
        ordering = ["order", "id"]
        verbose_name = _("Activity image")
        verbose_name_plural = _("Activity gallery")

    def __str__(self):
        return f"{self.activity} - {self.id}"