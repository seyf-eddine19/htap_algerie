from django.views.generic import DetailView, ListView

from .models import Activity


class LanguageMixin:
    language = "fr"

    def get_language(self):
        return getattr(self.request, "LANGUAGE_CODE", self.language)

    def get_translation(self, obj):
        language = self.get_language()

        translation = obj.translations.filter(
            language=language
        ).first()

        if translation:
            return translation

        return obj.translations.filter(
            language="fr"
        ).first()


class ActivityListView(LanguageMixin, ListView):
    model = Activity
    template_name = "activities/list.html"
    context_object_name = "activities"
    paginate_by = 9

    def get_queryset(self):
        return (
            Activity.objects
            .filter(status=Activity.Status.PUBLISHED)
            .prefetch_related("translations", "gallery")
            .order_by("-start_date", "-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["activity_translations"] = {
            activity.pk: self.get_translation(activity)
            for activity in context["activities"]
        }

        return context


class ActivityDetailView(LanguageMixin, DetailView):
    model = Activity
    template_name = "activities/detail.html"
    context_object_name = "activity"

    def get_queryset(self):
        return (
            Activity.objects
            .filter(status=Activity.Status.PUBLISHED)
            .prefetch_related(
                "translations",
                "translations__blocks",
                "gallery",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["translation"] = self.get_translation(
            self.object
        )

        return context