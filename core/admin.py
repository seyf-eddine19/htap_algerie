from django.contrib import admin
from .models import Member, ContactMessage


# @admin.register(AssociationInfo)
# class AssociationInfoAdmin(admin.ModelAdmin):
#     list_display = ("name", "phone", "email", "updated_at")

#     fieldsets = (
#         ("Identity", {
#             "fields": ("name", "full_name", "logo")
#         }),
#         ("About", {
#             "fields": ("description", "history", "mission", "objectives")
#         }),
#         ("Contact", {
#             "fields": ("address", "phone", "email", "map_url")
#         }),
#         ("Social media", {
#             "fields": ("facebook_url", "instagram_url", "youtube_url")
#         }),
#     )

#     readonly_fields = ("updated_at",)

#     def has_add_permission(self, request):
#         return not AssociationInfo.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         return False


# @admin.register(Statistic)
# class StatisticAdmin(admin.ModelAdmin):
#     list_display = ("title", "value", "order", "is_active")
#     list_filter = ("is_active",)
#     search_fields = ("title", "description")
#     list_editable = ("order", "is_active")
#     ordering = ("order",)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("display_name", "display_role", "order", "is_active")
    list_display_links = ("display_name",)
    list_filter = ("is_active",)
    list_editable = ("order", "is_active")
    search_fields = (
        "name",
        "name_ar",
        "role_ar",
        "role_en",
        "role_fr",
        "bio",
    )
    ordering = ("order", "name")
    readonly_fields = ("display_name", "display_role")

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "photo",
                    "bio",
                )
            },
        ),
        (
            "Arabic",
            {
                "fields": (
                    "name_ar",
                    "role_ar",
                )
            },
        ),
        (
            "English",
            {
                "fields": (
                    "role_en",
                )
            },
        ),
        (
            "French",
            {
                "fields": (
                    "role_fr",
                )
            },
        ),
        (
            "Display",
            {
                "fields": (
                    "display_name",
                    "display_role",
                )
            },
        ),
        (
            "Settings",
            {
                "fields": (
                    "order",
                    "is_active",
                )
            },
        ),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "first_name", "last_name", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "subject", "message")
    list_editable = ("status",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)

    fieldsets = (
        ("Sender", {
            "fields": ("first_name", "last_name", "email", "phone")
        }),
        ("Message", {
            "fields": ("subject", "message")
        }),
        ("Management", {
            "fields": ("status", "created_at", "updated_at")
        }),
    )