from django.contrib import admin
from .models import Article, ArticleCategory, ArticleTranslation, ArticleBlock


class ArticleTranslationInline(admin.StackedInline):
    model = ArticleTranslation
    extra = 1
    fields = ("language", "title", "excerpt", "meta_title", "meta_description")


class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1
    fields = ("block_type", "order", "title", "text", "image", "image_caption")
    ordering = ("order", "id")


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_active")
    ordering = ("order", "name")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("slug", "get_title", "category", "status", "is_featured", "published_at")
    list_filter = ("status", "is_featured", "category", "published_at")
    search_fields = ("slug", "author", "translations__title", "translations__excerpt")
    list_editable = ("status", "is_featured")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Article", {
            "fields": ("category", "featured_image", "author", "slug")
        }),
        ("Publication", {
            "fields": ("status", "is_featured", "published_at")
        }),
        ("System", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = (ArticleTranslationInline,)
    ordering = ("-published_at", "-created_at")

    @admin.display(description="Title")
    def get_title(self, obj):
        translation = obj.translations.first()
        return translation.title if translation else "-"


@admin.register(ArticleTranslation)
class ArticleTranslationAdmin(admin.ModelAdmin):
    list_display = ("title", "article", "language")
    list_filter = ("language",)
    search_fields = ("title", "excerpt", "meta_title", "meta_description")
    inlines = (ArticleBlockInline,)