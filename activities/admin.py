from django.contrib import admin
from .models import Activity, ActivityTranslation, ActivityBlock, ActivityImage


class ActivityTranslationInline(admin.StackedInline):
    model = ActivityTranslation
    extra = 1
    fields = ("language", "title", "excerpt", "meta_title", "meta_description")


class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1
    fields = ("image", "caption", "order")
    ordering = ("order", "id")


class ActivityBlockInline(admin.StackedInline):
    model = ActivityBlock
    extra = 1
    fields = ("block_type", "order", "title", "text", "image", "image_caption")
    ordering = ("order", "id")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("get_title", "activity_type", "status", "location", "start_date", "is_featured")
    list_filter = ("activity_type", "status", "is_featured", "start_date")
    search_fields = ("slug", "location", "translations__title", "translations__excerpt")
    list_editable = ("status", "is_featured")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Activity", {
            "fields": ("activity_type", "featured_image", "location", "slug")
        }),
        ("Date", {
            "fields": ("start_date", "end_date")
        }),
        ("Publication", {
            "fields": ("status", "is_featured")
        }),
        ("System", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = (ActivityTranslationInline, ActivityImageInline)
    ordering = ("-start_date", "-created_at")

    @admin.display(description="Title")
    def get_title(self, obj):
        translation = obj.translations.first()
        return translation.title if translation else "-"


@admin.register(ActivityTranslation)
class ActivityTranslationAdmin(admin.ModelAdmin):
    list_display = ("title", "activity", "language")
    list_filter = ("language",)
    search_fields = ("title", "excerpt", "meta_title", "meta_description")
    inlines = (ActivityBlockInline,)


@admin.register(ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
    list_display = ("activity", "caption", "order")
    search_fields = ("activity__translations__title", "caption")
    list_editable = ("order",)
    ordering = ("order", "id")