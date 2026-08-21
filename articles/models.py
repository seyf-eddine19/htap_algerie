from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _, get_language


class Language(models.TextChoices):
    ARABIC = "ar", _("العربية")
    ENGLISH = "en", _("English")
    FRENCH = "fr", _("Français")


class ArticleCategory(models.Model):
    name = models.CharField(_("name"), max_length=100)
    slug = models.SlugField(_("slug"), max_length=120, unique=True)
    is_active = models.BooleanField(_("active"), default=True, db_index=True)
    order = models.PositiveIntegerField(_("order"), default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = _("Article category")
        verbose_name_plural = _("Article categories")

    def __str__(self):
        return self.name


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")

    slug = models.SlugField(_("slug"), max_length=280, unique=True, blank=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="articles", verbose_name=_("category"))
    featured_image = models.ImageField(_("featured image"), upload_to="articles/%Y/%m/", blank=True, null=True)
    author = models.CharField(_("author"), max_length=150, blank=True)
    status = models.CharField(_("status"), max_length=20, choices=Status.choices, default=Status.DRAFT, db_index=True)
    is_featured = models.BooleanField(_("featured"), default=False, db_index=True)
    published_at = models.DateTimeField(_("published at"), null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def get_translation(self):
        if hasattr(self, "current_translation"):
            return self.current_translation[0] if self.current_translation else None

        lang = get_language()

        return (self.translations.filter(language=lang).first() or self.translations.first())

    def save(self, *args, **kwargs):
        # معالجة إنشاء الـ slug قبل أو مع أول عملية حفظ
        if not self.slug:
            translation = self.get_translation()
            if translation and translation.title:
                self.slug = slugify(translation.title, allow_unicode=True)
            else:
                self.slug = slugify(f"article-{self.pk or 'new'}", allow_unicode=True)
                
        super().save(*args, **kwargs)

    def __str__(self):
        translation = self.get_translation()
        return translation.title if translation else f"Article #{self.pk}"


class ArticleTranslation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="translations", verbose_name=_("article"))
    language = models.CharField(_("language"), max_length=2, choices=Language.choices)
    title = models.CharField(_("title"), max_length=250)
    excerpt = models.TextField(_("excerpt"), blank=True)
    meta_title = models.CharField(_("meta title"), max_length=250, blank=True)
    meta_description = models.CharField(_("meta description"), max_length=300, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["article", "language"], name="unique_article_language")
        ]
        verbose_name = _("Article translation")
        verbose_name_plural = _("Article translations")

    def __str__(self):
        return f"{self.title} ({self.language})"


class ArticleBlock(models.Model):
    class BlockType(models.TextChoices):
        HEADING = "heading", _("Heading")
        PARAGRAPH = "paragraph", _("Paragraph")
        QUOTE = "quote", _("Quote")
        CALLOUT = "callout", _("Callout")
        DIVIDER = "divider", _("Divider")
        IMAGE = "image", _("Image")
        VIDEO = "video", _("Video")
        DOCUMENT = "document", _("Document")
        EMBED = "embed", _("Embed")
        BUTTON = "button", _("Button")

    translation = models.ForeignKey(ArticleTranslation, on_delete=models.CASCADE, related_name="blocks", verbose_name=_("translation"))
    block_type = models.CharField(_("block type"), max_length=20, choices=BlockType.choices)
    order = models.PositiveIntegerField(_("order"), default=0)

    # General content
    title = models.CharField(_("title"), max_length=250, blank=True)
    text = models.TextField(_("text"), blank=True)
    caption = models.CharField(_("caption"), max_length=300, blank=True)

    # Files
    image = models.ImageField(_("image"), upload_to="articles/blocks/%Y/%m/", blank=True, null=True)
    document = models.FileField(_("document"), upload_to="articles/documents/%Y/%m/", blank=True, null=True)

    # URLs
    url = models.URLField(_("URL"), blank=True)

    heading_level = models.CharField(_("heading level"), max_length=2, choices=[("h2", "H2"), ("h3", "H3"), ("h4", "H4")], blank=True)
    callout_style = models.CharField(_("callout style"), max_length=20, choices=[("info", _("Information")), ("success", _("Success")), ("warning", _("Warning")), ("danger", _("Danger"))], blank=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = _("Content block")
        verbose_name_plural = _("Content blocks")

    def __str__(self):
        return f"{self.translation.title} - {self.get_block_type_display()}"

