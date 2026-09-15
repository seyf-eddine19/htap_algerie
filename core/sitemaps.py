from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import override

from articles.models import Article, ArticleTranslation
from activities.models import Activity, ActivityTranslation


class MultilingualSitemap(Sitemap):
    """
    Base sitemap for multilingual URLs.

    Each item is:
        (object, language_code)
    """

    def _build_items(self, objects, translation_model, relation_field):
        items = []

        language_codes = [code for code, _ in settings.LANGUAGES]

        for obj in objects:
            available_languages = set(
                translation_model.objects.filter(
                    **{relation_field: obj}
                ).values_list("language", flat=True)
            )

            for language_code in language_codes:
                if language_code in available_languages:
                    items.append((obj, language_code))

        return items

    def lastmod(self, item):
        obj, _ = item
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        items = []

        for language_code, _ in settings.LANGUAGES:
            for view_name in [
                "core:home",
                "core:about",
                "core:htap",
                "core:help",
                "core:membership",
                "core:contact",
            ]:
                items.append((view_name, language_code))

        return items

    def location(self, item):
        view_name, language_code = item

        with override(language_code):
            return reverse(view_name)


class ArticleSitemap(MultilingualSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        articles = Article.objects.filter(
            status="published"
        ).order_by("-updated_at")

        return self._build_items(
            articles,
            ArticleTranslation,
            "article",
        )

    def location(self, item):
        article, language_code = item

        with override(language_code):
            return reverse(
                "articles:detail",
                kwargs={"slug": article.slug},
            )


class ActivitySitemap(MultilingualSitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        activities = Activity.objects.filter(
            status="published"
        ).order_by("-updated_at")

        return self._build_items(
            activities,
            ActivityTranslation,
            "activity",
        )

    def location(self, item):
        activity, language_code = item

        with override(language_code):
            return reverse(
                "activities:detail",
                kwargs={"slug": activity.slug},
            )