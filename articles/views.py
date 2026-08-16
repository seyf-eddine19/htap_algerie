from django.views.generic import DetailView, ListView

from .models import Article


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


class ArticleListView(LanguageMixin, ListView):
    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 9

    def get_queryset(self):
        return (
            Article.objects
            .filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related("translations")
            .order_by("-published_at", "-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["article_translations"] = {
            article.pk: self.get_translation(article)
            for article in context["articles"]
        }

        return context


class ArticleDetailView(LanguageMixin, DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return (
            Article.objects
            .filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related(
                "translations",
                "translations__blocks",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["translation"] = self.get_translation(
            self.object
        )

        return context




from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.views.generic import DetailView, ListView

from .models import Article, ArticleCategory, ArticleTranslation, Language


def get_current_language():
    """Récupère le code de langue courante ou la langue par défaut (FR)."""
    lang = get_language()
    if lang and "-" in lang:
        lang = lang.split("-")[0]
    valid_langs = [choices[0] for choices in Language.choices]
    return lang if lang in valid_langs else Language.FRENCH


class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 9

    def get_queryset(self):
        current_lang = get_current_language()

        # Prefetch de la traduction appropriée selon la langue courante
        translations_qs = ArticleTranslation.objects.filter(
            language=current_lang
        )

        queryset = (
            Article.objects.filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "translations",
                    queryset=translations_qs,
                    to_attr="current_translation",
                )
            )
        )

        # Filtrage par catégorie
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Recherche par mot-clé
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(translations__title__icontains=search_query)
                | Q(translations__excerpt__icontains=search_query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_lang = get_current_language()

        context["categories"] = ArticleCategory.objects.filter(
            is_active=True
        ).order_by("order")
        context["selected_category"] = self.request.GET.get("category", "")
        context["search_query"] = self.request.GET.get("q", "")

        # Article à la une (Featured)
        featured_qs = (
            Article.objects.filter(
                status=Article.Status.PUBLISHED, is_featured=True
            )
            .prefetch_related(
                Prefetch(
                    "translations",
                    queryset=ArticleTranslation.objects.filter(
                        language=current_lang
                    ),
                    to_attr="current_translation",
                )
            )
            .first()
        )
        context["featured_article"] = featured_qs
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        current_lang = get_current_language()

        translations_qs = ArticleTranslation.objects.filter(
            language=current_lang
        ).prefetch_related("blocks")

        return (
            Article.objects.filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "translations",
                    queryset=translations_qs,
                    to_attr="current_translation",
                )
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_lang = get_current_language()
        article = self.get_object()

        # Attachement de la traduction courante
        translation = (
            article.current_translation[0]
            if getattr(article, "current_translation", None)
            else article.translations.first()
        )

        context["translation"] = translation
        context["blocks"] = (
            translation.blocks.all().order_by("order") if translation else []
        )

        # Articles similaires dans la même catégorie
        if article.category:
            context["related_articles"] = (
                Article.objects.filter(
                    status=Article.Status.PUBLISHED, category=article.category
                )
                .exclude(id=article.id)
                .prefetch_related(
                    Prefetch(
                        "translations",
                        queryset=ArticleTranslation.objects.filter(
                            language=current_lang
                        ),
                        to_attr="current_translation",
                    )
                )[:3]
            )

        return context