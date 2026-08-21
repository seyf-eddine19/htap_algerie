# dashboard/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Permission, User
from django.core.exceptions import PermissionDenied

from django.db import transaction
from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from core.models import Member, ContactMessage
from articles.models import (
    Language, Article, ArticleCategory, ArticleTranslation, ArticleBlock,
)
from activities.models import (
    Activity, ActivityType, ActivityTranslation, ActivityBlock, ActivityImage,
)
from activities.forms import ( 
    ActivityForm, ActivityTranslationFormSet, ActivityImageFormSet, ActivityBlockForm,
)
from .mixins import DashboardAccessMixin, DashboardBaseMixin, DashboardPermissionMixin

    
# ============================================================
# DASHBOARD HOME
# ============================================================

class DashboardHomeView(DashboardAccessMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["members_count"] = Member.objects.count()
        context["active_members_count"] = Member.objects.filter(
            is_active=True
        ).count()

        context["articles_count"] = Article.objects.count()
        context["published_articles_count"] = Article.objects.filter(
            status=Article.Status.PUBLISHED
        ).count()

        context["categories_count"] = ArticleCategory.objects.count()

        context["activities_count"] = Activity.objects.count()
        context["published_activities_count"] = Activity.objects.filter(
            status=Activity.Status.PUBLISHED
        ).count()

        context["messages_count"] = ContactMessage.objects.count()
        context["new_messages_count"] = ContactMessage.objects.filter(
            status=ContactMessage.Status.NEW
        ).count()

        context["recent_articles"] = (
            Article.objects
            .select_related("category")
            .prefetch_related("translations")
            .order_by("-created_at")[:5]
        )

        context["recent_activities"] = (
            Activity.objects
            .prefetch_related("translations")
            .order_by("-created_at")[:5]
        )

        context["recent_messages"] = (
            ContactMessage.objects
            .order_by("-created_at")[:5]
        )

        return context


# ============================================================
# USERS
# ============================================================

# class UserListView(DashboardBaseMixin, ListView):
#     model = User
#     template_name = "accounts/users/list.html"
#     context_object_name = "users"
#     permission_required = "auth.view_user"

#     def get_queryset(self):
#         return User.objects.order_by("username")


# class UserCreateView(DashboardBaseMixin, CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = "accounts/users/form.html"
#     success_url = reverse_lazy("accounts:user_list")
#     permission_required = "auth.add_user"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = _("Create User")
#         return context

#     def form_valid(self, form):
#         messages.success(self.request, _("User created successfully."))
#         return super().form_valid(form)


# class UserUpdateView(DashboardBaseMixin, UpdateView):
#     model = User
#     form_class = UserChangeForm
#     template_name = "accounts/users/form.html"
#     context_object_name = "user_obj"
#     success_url = reverse_lazy("accounts:user_list")
#     permission_required = "auth.change_user"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = _("Update User")
#         return context

#     def form_valid(self, form):
#         messages.success(self.request, _("User updated successfully."))
#         return super().form_valid(form)


# class UserDeleteView(DashboardBaseMixin, DeleteView):
#     model = User
#     template_name = "accounts/users/delete.html"
#     context_object_name = "user_obj"
#     success_url = reverse_lazy("accounts:user_list")
#     permission_required = "auth.delete_user"

#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()

#         if self.object == request.user:
#             messages.error(request, _("You cannot delete your own account."))
#             return redirect(self.success_url)

#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         username = self.object.username
#         response = super().form_valid(form)

#         messages.success(
#             self.request,
#             _("User '%(username)s' was deleted successfully.") % {
#                 "username": username
#             },
#         )

#         return response


# class UserPermissionsView(DashboardBaseMixin, UpdateView):
#     model = User
#     template_name = "accounts/users/permissions.html"
#     context_object_name = "user_obj"
#     fields = []
#     permission_required = "auth.change_user"

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_superuser:
#             raise PermissionDenied

#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context["permissions"] = (
#             Permission.objects
#             .select_related("content_type")
#             .order_by(
#                 "content_type__app_label",
#                 "content_type__model",
#                 "codename",
#             )
#         )

#         context["user_permissions"] = set(
#             self.object.user_permissions.values_list("id", flat=True)
#         )

#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()

#         self.object.is_active = "is_active" in request.POST
#         self.object.is_staff = "is_staff" in request.POST

#         self.object.user_permissions.set(
#             request.POST.getlist("permissions")
#         )

#         self.object.save()

#         messages.success(
#             request,
#             _("User permissions updated successfully."),
#         )

#         return redirect("accounts:user_list")


# ============================================================
# MEMBERS
# ============================================================

class MemberListView(DashboardAccessMixin, ListView):
    model = Member
    template_name = "dashboard/members/list.html"
    context_object_name = "members"
    paginate_by = 20

    def get_queryset(self):
        queryset = Member.objects.all().order_by("order", "name")

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(name_ar__icontains=search)
                | Q(role_fr__icontains=search)
                | Q(role_en__icontains=search)
                | Q(role_ar__icontains=search)
            )

        status = self.request.GET.get("status")

        if status == "active":
            queryset = queryset.filter(is_active=True)

        elif status == "inactive":
            queryset = queryset.filter(is_active=False)

        return queryset

class MemberCreateView(DashboardBaseMixin, CreateView):
    model = Member
    template_name = "dashboard/members/form.html"
    fields = [
        "name",
        "name_ar",
        "role_ar",
        "role_en",
        "role_fr",
        "photo",
        "bio",
        "order",
        "is_active",
    ]
    success_url = reverse_lazy("dashboard:members")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Member created successfully."
        )
        return super().form_valid(form)

class MemberUpdateView(DashboardBaseMixin, UpdateView):
    model = Member
    template_name = "dashboard/members/form.html"
    fields = [
        "name",
        "name_ar",
        "role_ar",
        "role_en",
        "role_fr",
        "photo",
        "bio",
        "order",
        "is_active",
    ]
    success_url = reverse_lazy("dashboard:members")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Member updated successfully."
        )
        return super().form_valid(form)

class MemberDeleteView(DashboardAccessMixin, DeleteView):
    model = Member
    template_name = "dashboard/members/delete.html"
    success_url = reverse_lazy("dashboard:members")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Member deleted successfully."
        )
        return super().form_valid(form)


# ============================================================
# ARTICLES
# ============================================================
class ArticleListView(DashboardAccessMixin, ListView):
    model = Article
    template_name = "dashboard/articles/list.html"
    context_object_name = "articles"
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            Article.objects
            .select_related("category")
            .prefetch_related("translations")
            .order_by("-published_at", "-created_at")
        )

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(slug__icontains=search)
                | Q(author__icontains=search)
                | Q(translations__title__icontains=search)
            ).distinct()

        status = self.request.GET.get("status")

        if status in [
            Article.Status.DRAFT,
            Article.Status.PUBLISHED,
        ]:
            queryset = queryset.filter(status=status)

        category = self.request.GET.get("category")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ArticleCategory.objects.filter(
            is_active=True
        )

        return context

class ArticleCreateView(DashboardBaseMixin, CreateView):
    model = Article
    template_name = "dashboard/articles/form.html"
    fields = [
        "category",
        "featured_image",
        "author",
        "status",
        "is_featured",
        "published_at",
    ]
    success_url = reverse_lazy("dashboard:articles")

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Article created successfully."
        )

        return response

class ArticleUpdateView(DashboardBaseMixin, UpdateView):
    model = Article
    template_name = "dashboard/articles/form.html"
    fields = [
        "category",
        "featured_image",
        "author",
        "status",
        "is_featured",
        "published_at",
    ]
    success_url = reverse_lazy("dashboard:articles")

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Article updated successfully."
        )

        return response

class ArticleDeleteView(DashboardAccessMixin, DeleteView):
    model = Article
    template_name = "dashboard/articles/delete.html"
    success_url = reverse_lazy("dashboard:articles")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Article deleted successfully."
        )
        return super().form_valid(form)



from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from articles.forms import ArticleForm, ArticleTranslationFormSet

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "dashboard/articles/form.html"
    success_url = reverse_lazy("dashboard:articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["translation_formset"] = ArticleTranslationFormSet(self.request.POST, self.request.FILES)
        else:
            # Pre-populate translation forms for all supported languages
            initial_translations = [{'language': lang_code} for lang_code, _ in Language.choices]
            context["translation_formset"] = ArticleTranslationFormSet(
                initial=initial_translations
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        translation_formset = context["translation_formset"]

        if translation_formset.is_valid():
            with transaction.atomic():
                self.object = form.save()
                translation_formset.instance = self.object
                translations = translation_formset.save()

                # Save fallback/primary slug based on the default translation title if not auto-generated
                if not self.object.slug and translations:
                    primary_trans = translations[0]
                    from django.utils.text import slugify
                    self.object.slug = slugify(primary_trans.title)
                    self.object.save()

                # Process Alpine.js visual content blocks
                self._process_content_blocks(translations)

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def _process_content_blocks(self, translations):
        """
        Parses blocks supplied in the POST payload and associates them
        with their corresponding translation instances.
        """
        # Map language codes to translation instances
        trans_map = {t.language: t for t in translations}

        # Clear existing blocks on update operations
        ArticleBlock.objects.filter(translation__in=translations).delete()

        # Parse block dynamic inputs from request POST and FILES
        # Example processing loop depending on how payload keys are organized
        block_count = int(self.request.POST.get("blocks-TOTAL_FORMS", 0))
        for i in range(block_count):
            lang_code = self.request.POST.get(f"blocks-{i}-language", Language.ARABIC)
            translation = trans_map.get(lang_code)
            
            if translation:
                ArticleBlock.objects.create(
                    translation=translation,
                    block_type=self.request.POST.get(f"blocks-{i}-block_type"),
                    order=i,
                    title=self.request.POST.get(f"blocks-{i}-title", ""),
                    text=self.request.POST.get(f"blocks-{i}-text", ""),
                    caption=self.request.POST.get(f"blocks-{i}-caption", ""),
                    url=self.request.POST.get(f"blocks-{i}-url", ""),
                    heading_level=self.request.POST.get(f"blocks-{i}-heading_level", ""),
                    callout_style=self.request.POST.get(f"blocks-{i}-callout_style", ""),
                    image=self.request.FILES.get(f"blocks-{i}-image"),
                    document=self.request.FILES.get(f"blocks-{i}-document"),
                )

    def _process_content_blocks(self, translations):
        # If updating an existing article, delete existing blocks first (or handle updates)
        for trans in translations:
            trans.blocks.all().delete()

        try:
            block_count = int(self.request.POST.get('blocks-TOTAL_FORMS', 0))
        except (ValueError, TypeError):
            block_count = 0

        trans_map = {t.language: t for t in translations}

        for i in range(block_count):
            block_type = self.request.POST.get(f'blocks-{i}-block_type')
            lang_code = self.request.POST.get(f'blocks-{i}-language')

            # FIX: Skip processing if block_type or lang_code is missing
            if not block_type or not lang_code:
                continue

            translation = trans_map.get(lang_code)
            if not translation:
                continue

            ArticleBlock.objects.create(
                translation=translation,
                block_type=block_type,  # Guaranteed non-null
                order=i,
                title=self.request.POST.get(f'blocks-{i}-title', ''),
                text=self.request.POST.get(f'blocks-{i}-text', ''),
                caption=self.request.POST.get(f'blocks-{i}-caption', ''),
                url=self.request.POST.get(f'blocks-{i}-url', ''),
                heading_level=self.request.POST.get(f'blocks-{i}-heading_level', 'h2'),
                callout_style=self.request.POST.get(f'blocks-{i}-callout_style', 'info'),
                image=self.request.FILES.get(f'blocks-{i}-image'),
                document=self.request.FILES.get(f'blocks-{i}-document'),
            )


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "dashboard/articles/form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("dashboard:articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["translation_formset"] = ArticleTranslationFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context["translation_formset"] = ArticleTranslationFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        translation_formset = context["translation_formset"]

        if translation_formset.is_valid():
            with transaction.atomic():
                self.object = form.save()
                translations = translation_formset.save()

                # Process updated blocks
                trans_list = list(self.object.translations.all())
                ArticleCreateView._process_content_blocks(self, trans_list)

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

# ============================================================
# ARTICLE CATEGORIES
# ============================================================
class ArticleCategoryListView(DashboardAccessMixin, ListView):
    model = ArticleCategory
    template_name = "dashboard/categories/list.html"
    context_object_name = "categories"
    paginate_by = 30

    def get_queryset(self):
        queryset = (
            ArticleCategory.objects
            .annotate(article_count=Count("articles"))
            .order_by("order", "name")
        )

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(slug__icontains=search)
            )

        return queryset

class ArticleCategoryCreateView(DashboardBaseMixin, CreateView):
    model = ArticleCategory
    template_name = "dashboard/categories/form.html"
    fields = [
        "name",
        "slug",
        "is_active",
        "order",
    ]
    success_url = reverse_lazy("dashboard:categories")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Category created successfully."
        )
        return super().form_valid(form)

class ArticleCategoryUpdateView(DashboardBaseMixin, UpdateView):
    model = ArticleCategory
    template_name = "dashboard/categories/form.html"
    fields = [
        "name",
        "slug",
        "is_active",
        "order",
    ]
    success_url = reverse_lazy("dashboard:categories")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Category updated successfully."
        )
        return super().form_valid(form)

class ArticleCategoryDeleteView(DashboardAccessMixin, DeleteView):
    model = ArticleCategory
    template_name = "dashboard/categories/delete.html"
    success_url = reverse_lazy("dashboard:categories")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Category deleted successfully."
        )
        return super().form_valid(form)



class ArticleCategoryManageView(DashboardAccessMixin, ListView):
    model = ArticleCategory
    template_name = "dashboard/categories/manage.html"
    context_object_name = "categories"
    paginate_by = 30

    def get_queryset(self):
        queryset = (
            ArticleCategory.objects
            .annotate(article_count=Count("articles"))
            .order_by("order", "name")
        )

        search = self.request.GET.get("q", "").strip()

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(slug__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.request.GET.get("edit")

        if category_id:
            context["edit_category"] = get_object_or_404(
                ArticleCategory,
                pk=category_id
            )

        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "create":
            return self.create_category(request)

        if action == "update":
            return self.update_category(request)

        if action == "delete":
            return self.delete_category(request)

        messages.error(request, "Invalid action.")
        return redirect("dashboard:categories")

    def create_category(self, request):
        name = request.POST.get("name", "").strip()
        slug = request.POST.get("slug", "").strip()
        is_active = request.POST.get("is_active") == "on"
        order = request.POST.get("order", "0").strip()

        if not name:
            messages.error(request, "Category name is required.")
            return redirect("dashboard:categories")

        if not slug:
            messages.error(request, "Category slug is required.")
            return redirect("dashboard:categories")

        if ArticleCategory.objects.filter(slug=slug).exists():
            messages.error(
                request,
                "A category with this slug already exists."
            )
            return redirect("dashboard:categories")

        try:
            order = int(order)
        except (TypeError, ValueError):
            order = 0

        ArticleCategory.objects.create(
            name=name,
            slug=slug,
            is_active=is_active,
            order=order,
        )

        messages.success(
            request,
            "Category created successfully."
        )

        return redirect("dashboard:categories")

    def update_category(self, request):
        category_id = request.POST.get("category_id")

        category = get_object_or_404(
            ArticleCategory,
            pk=category_id
        )

        name = request.POST.get("name", "").strip()
        slug = request.POST.get("slug", "").strip()
        is_active = request.POST.get("is_active") == "on"
        order = request.POST.get("order", "0").strip()

        if not name:
            messages.error(request, "Category name is required.")
            return redirect("dashboard:categories")

        if not slug:
            messages.error(request, "Category slug is required.")
            return redirect(
                f"{request.path}?edit={category.pk}"
            )

        if ArticleCategory.objects.filter(
            slug=slug
        ).exclude(
            pk=category.pk
        ).exists():
            messages.error(
                request,
                "A category with this slug already exists."
            )
            return redirect(
                f"{request.path}?edit={category.pk}"
            )

        try:
            order = int(order)
        except (TypeError, ValueError):
            order = 0

        category.name = name
        category.slug = slug
        category.is_active = is_active
        category.order = order
        category.save()

        messages.success(
            request,
            "Category updated successfully."
        )

        return redirect("dashboard:categories")

    def delete_category(self, request):
        category_id = request.POST.get("category_id")

        category = get_object_or_404(
            ArticleCategory,
            pk=category_id
        )

        category.delete()

        messages.success(
            request,
            "Category deleted successfully."
        )

        return redirect("dashboard:categories")

# ============================================================
# ACTIVITIES
# ============================================================
class ActivityListView(DashboardAccessMixin, ListView):
    model = Activity
    template_name = "dashboard/activities/list.html"
    context_object_name = "activities"
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            Activity.objects
            .prefetch_related("translations")
            .order_by("-start_date", "-created_at")
        )

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(slug__icontains=search)
                | Q(location__icontains=search)
                | Q(translations__title__icontains=search)
                | Q(translations__excerpt__icontains=search)
            ).distinct()

        status = self.request.GET.get("status")

        if status in Activity.Status.values:
            queryset = queryset.filter(status=status)

        activity_type = self.request.GET.get("type")

        if activity_type in ActivityType.values:
            queryset = queryset.filter(activity_type=activity_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["activity_types"] = ActivityType.choices
        context["statuses"] = Activity.Status.choices

        return context

class ActivityCreateView(DashboardBaseMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "dashboard/activities/form.html"
    success_url = reverse_lazy("dashboard:activities")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context["translation_formset"] = ActivityTranslationFormSet(
                self.request.POST,
                instance=self.object,
            )
            context["image_formset"] = ActivityImageFormSet(
                self.request.POST,
                self.request.FILES,
                instance=self.object,
            )
        else:
            context["translation_formset"] = ActivityTranslationFormSet(
                instance=self.object,
            )
            context["image_formset"] = ActivityImageFormSet(
                instance=self.object,
            )

        context["block_forms"] = []

        return context

    def form_valid(self, form):
        translation_formset = ActivityTranslationFormSet(
            self.request.POST,
            instance=self.object,
        )

        image_formset = ActivityImageFormSet(
            self.request.POST,
            self.request.FILES,
            instance=self.object,
        )

        if not translation_formset.is_valid():
            return self.form_invalid(form)

        if not image_formset.is_valid():
            return self.form_invalid(form)

        with transaction.atomic():
            self.object = form.save()

            translation_formset.instance = self.object
            translations = translation_formset.save()

            image_formset.instance = self.object
            image_formset.save()

            for translation in translations:
                prefix = f"blocks-{translation.language}"

                block_form = ActivityBlockForm(
                    self.request.POST,
                    self.request.FILES,
                    prefix=prefix,
                    instance=None,
                )

                if block_form.is_valid():
                    blocks = block_form.save(commit=False)

                    for block in blocks:
                        block.translation = translation
                        block.save()

        messages.success(
            self.request,
            "Activity created successfully."
        )

        return redirect(self.success_url)

class ActivityUpdateView(DashboardBaseMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = "dashboard/activities/form.html"
    success_url = reverse_lazy("dashboard:activities")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context["translation_formset"] = ActivityTranslationFormSet(
                self.request.POST,
                instance=self.object,
            )
            context["image_formset"] = ActivityImageFormSet(
                self.request.POST,
                self.request.FILES,
                instance=self.object,
            )
        else:
            context["translation_formset"] = ActivityTranslationFormSet(
                instance=self.object,
            )
            context["image_formset"] = ActivityImageFormSet(
                instance=self.object,
            )

        return context

    def form_valid(self, form):
        translation_formset = ActivityTranslationFormSet(
            self.request.POST,
            instance=self.object,
        )

        image_formset = ActivityImageFormSet(
            self.request.POST,
            self.request.FILES,
            instance=self.object,
        )

        if not translation_formset.is_valid():
            return self.form_invalid(form)

        if not image_formset.is_valid():
            return self.form_invalid(form)

        with transaction.atomic():
            self.object = form.save()

            translation_formset.instance = self.object
            translation_formset.save()

            image_formset.instance = self.object
            image_formset.save()

        messages.success(
            self.request,
            "Activity updated successfully."
        )

        return redirect(self.success_url)

class ActivityDeleteView(DashboardAccessMixin, DeleteView):
    model = Activity
    template_name = "dashboard/activities/delete.html"
    success_url = reverse_lazy("dashboard:activities")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Activity deleted successfully."
        )
        return super().form_valid(form)


# ============================================================
# CONTACT MESSAGES
# ============================================================
class ContactMessageListView(DashboardAccessMixin, ListView):
    model = ContactMessage
    template_name = "dashboard/messages/list.html"
    context_object_name = "messages_list"
    paginate_by = 25

    def get_queryset(self):
        queryset = ContactMessage.objects.all()

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
                | Q(subject__icontains=search)
                | Q(message__icontains=search)
            )

        status = self.request.GET.get("status")

        if status in [
            ContactMessage.Status.NEW,
            ContactMessage.Status.READ,
            ContactMessage.Status.REPLIED,
            ContactMessage.Status.ARCHIVED,
        ]:
            queryset = queryset.filter(status=status)

        return queryset

class ContactMessageDetailView(DashboardAccessMixin, DetailView):
    model = ContactMessage
    template_name = "dashboard/messages/detail.html"
    context_object_name = "contact_message"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        # Automatically mark a new message as read
        if obj.status == ContactMessage.Status.NEW:
            obj.status = ContactMessage.Status.READ
            obj.save(update_fields=["status", "updated_at"])

        return obj

class ContactMessageStatusView(DashboardAccessMixin, View):
    """
    Change message status.

    POST:
        status=new
        status=read
        status=replied
        status=archived
    """

    def post(self, request, pk):
        contact_message = ContactMessage.objects.get(pk=pk)

        status = request.POST.get("status")

        valid_statuses = {
            value for value, label in ContactMessage.Status.choices
        }

        if status not in valid_statuses:
            messages.error(
                request,
                "Invalid message status."
            )
            return redirect(
                "dashboard:message_detail",
                pk=contact_message.pk,
            )

        contact_message.status = status
        contact_message.save(
            update_fields=["status", "updated_at"]
        )

        messages.success(
            request,
            "Message status updated successfully."
        )

        return redirect(
            "dashboard:message_detail",
            pk=contact_message.pk,
        )

class ContactMessageDeleteView(DashboardAccessMixin, DeleteView):
    model = ContactMessage
    template_name = "dashboard/messages/delete.html"
    success_url = reverse_lazy("dashboard:messages")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Message deleted successfully."
        )
        return super().form_valid(form)

