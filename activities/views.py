from django.utils.translation import get_language
from django.views.generic import DetailView, ListView

from .models import Activity, ActivityType, Language


def get_activity_language():
    language = get_language() or Language.ENGLISH

    if language not in dict(Language.choices):
        language = Language.ENGLISH

    return language


def get_activity_translation(activity, language):
    return (
        activity.translations.filter(language=language).first()
        or activity.translations.filter(language=Language.ENGLISH).first()
        or activity.translations.filter(language=Language.FRENCH).first()
        or activity.translations.filter(language=Language.ARABIC).first()
        or activity.translations.first()
    )


class ActivityListView(ListView):
    model = Activity
    template_name = "activities/list.html"
    context_object_name = "activities"
    paginate_by = 9

    def get_queryset(self):
        queryset = (
            Activity.objects
            .filter(status=Activity.Status.PUBLISHED)
            .prefetch_related("translations", "gallery")
            .order_by("-start_date", "-created_at")
        )

        activity_type = self.request.GET.get("type", "").strip()

        if activity_type in dict(ActivityType.choices):
            queryset = queryset.filter(activity_type=activity_type)

        featured_id = (
            Activity.objects
            .filter(
                status=Activity.Status.PUBLISHED,
                is_featured=True,
            )
            .values_list("id", flat=True)
            .first()
        )

        if featured_id:
            queryset = queryset.exclude(id=featured_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        language = get_activity_language()

        for activity in context["activities"]:
            activity.active_translation = get_activity_translation(
                activity,
                language,
            )

        featured_activity = (
            Activity.objects
            .filter(
                status=Activity.Status.PUBLISHED,
                is_featured=True,
            )
            .prefetch_related("translations")
            .order_by("-start_date", "-created_at")
            .first()
        )

        if featured_activity:
            featured_activity.active_translation = get_activity_translation(
                featured_activity,
                language,
            )

        context["featured_activity"] = featured_activity
        context["activity_types"] = ActivityType.choices
        context["selected_type"] = self.request.GET.get("type", "").strip()
        context["current_language"] = language

        return context

    
class ActivityDetailView(DetailView):
    model = Activity
    template_name = "activities/detail.html"
    context_object_name = "activity"

    def get_queryset(self):
        return (
            Activity.objects
            .filter(status=Activity.Status.PUBLISHED)
            .prefetch_related(
                "translations__blocks",
                "gallery",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        language = get_activity_language()

        translation = get_activity_translation(
            self.object,
            language,
        )

        context["translation"] = translation
        context["current_language"] = language

        return context
