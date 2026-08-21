from django.db.models import Case, Prefetch, Q, Value, When
from django.utils.translation import get_language
from django.views.generic import DetailView, ListView

from .models import Article, ArticleCategory, ArticleTranslation, ArticleBlock, Language


def get_current_language():
    lang = get_language()

    if lang and "-" in lang:
        lang = lang.split("-")[0]

    valid_langs = [choice[0] for choice in Language.choices]

    return lang if lang in valid_langs else Language.FRENCH


def get_translation_prefetch(current_lang):
    return Prefetch(
        "translations",
        queryset=(
            ArticleTranslation.objects
            .annotate(
                is_current=Case(
                    When(
                        language=current_lang,
                        then=Value(0),
                    ),
                    default=Value(1),
                )
            )
            .order_by("is_current")
        ),
        to_attr="current_translation",
    )


class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 9

    def get_queryset(self):
        current_lang = get_current_language()

        queryset = (
            Article.objects.filter(status=Article.Status.PUBLISHED)
            .select_related("category")
            .prefetch_related(get_translation_prefetch(current_lang))
        )

        # التصفية بحسب التصنيف
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # البحث بكلمة مفتاحية
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

        # المقال المميز (Featured)
        context["featured_article"] = (
            Article.objects.filter(
                status=Article.Status.PUBLISHED, is_featured=True
            )
            .select_related("category")
            .prefetch_related(get_translation_prefetch(current_lang))
            .first()
        )
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        current_lang = get_current_language()

        translations_qs = (
            ArticleTranslation.objects
            .annotate(
                is_current=Case(
                    When(
                        language=current_lang,
                        then=Value(0),
                    ),
                    default=Value(1),
                )
            )
            .order_by("is_current")
            .prefetch_related(
                Prefetch(
                    "blocks",
                    queryset=ArticleBlock.objects.order_by(
                        "order",
                        "id",
                    ),
                )
            )
        )

        return (
            Article.objects
            .filter(status=Article.Status.PUBLISHED)
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

        article = self.object
        current_lang = get_current_language()

        # --------------------------------
        # Current translation
        # --------------------------------
        translations = getattr(
            article,
            "current_translation",
            [],
        )

        translation = (
            translations[0]
            if translations
            else None
        )

        context["translation"] = translation

        # --------------------------------
        # Blocks
        # --------------------------------
        context["blocks"] = (
            translation.blocks.all()
            if translation
            else []
        )

        # --------------------------------
        # Related articles
        # --------------------------------
        if article.category_id:
            context["related_articles"] = (
                Article.objects
                .filter(
                    status=Article.Status.PUBLISHED,
                    category_id=article.category_id,
                )
                .exclude(id=article.id)
                .select_related("category")
                .prefetch_related(
                    get_translation_prefetch(current_lang)
                )
                .order_by("-published_at")[:3]
            )
        else:
            context["related_articles"] = []

        return context


    