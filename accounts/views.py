from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, FormView, ListView, UpdateView, View

from django.contrib.auth import get_user_model

from dashboard.mixins import DashboardBaseMixin, DashboardPermissionMixin

from .forms import (
    AccountPasswordChangeForm, AccountUpdateForm, UserCreateForm, UserUpdateForm,
)

User = get_user_model()


class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:home")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()

        if not user.is_active:
            messages.error(
                self.request,
                _("Your account is inactive.")
            )
            return self.form_invalid(form)

        login(self.request, user)

        messages.success(
            self.request,
            _("Welcome back, %(username)s.") % {
                "username": user.get_username()
            }
        )

        next_url = (
            self.request.POST.get("next")
            or self.request.GET.get("next")
        )

        return redirect(next_url or "dashboard:home")


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)

        messages.success(
            request,
            _("You have been logged out successfully.")
        )

        return redirect("accounts:login")

    def get(self, request, *args, **kwargs):
        return redirect("accounts:login")


class UserListView(DashboardPermissionMixin, ListView):
    model = User
    template_name = "accounts/users/list.html"
    context_object_name = "users"
    permission_required = "auth.view_user"
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            User.objects
            # .select_related("member")
            .order_by("username")
        )

        query = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "").strip()

        if query:
            queryset = queryset.filter(
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(email__icontains=query)
            )

        if status == "active":
            queryset = queryset.filter(is_active=True)

        elif status == "inactive":
            queryset = queryset.filter(is_active=False)

        return queryset


class UserCreateView(DashboardPermissionMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "accounts/users/form.html"
    success_url = reverse_lazy("accounts:user_list")
    permission_required = "auth.add_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create User")
        context["is_create"] = True
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            _("User created successfully.")
        )
        return super().form_valid(form)


class UserUpdateView(DashboardPermissionMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "accounts/users/form.html"
    context_object_name = "user_obj"
    success_url = reverse_lazy("accounts:user_list")
    permission_required = "auth.change_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update User")
        context["is_create"] = False
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            _("User updated successfully.")
        )
        return super().form_valid(form)


class UserDeleteView(DashboardPermissionMixin, DeleteView):
    model = User
    template_name = "accounts/users/delete.html"
    context_object_name = "user_obj"
    success_url = reverse_lazy("accounts:user_list")
    permission_required = "auth.delete_user"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object == request.user:
            messages.error(
                request,
                _("You cannot delete your own account.")
            )
            return redirect("accounts:user_list")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = self.object.username

        response = super().form_valid(form)

        messages.success(
            self.request,
            _("User '%(username)s' was deleted successfully.") % {
                "username": username
            }
        )

        return response


class UserPermissionsView(DashboardPermissionMixin, UpdateView):
    model = User
    template_name = "accounts/users/permissions.html"
    context_object_name = "user_obj"
    fields = []
    permission_required = "auth.change_user"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["permissions"] = (
            Permission.objects
            .select_related("content_type")
            .order_by(
                "content_type__app_label",
                "content_type__model",
                "codename",
            )
        )

        context["user_permissions"] = set(
            self.object.user_permissions.values_list(
                "id",
                flat=True
            )
        )

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.is_active = "is_active" in request.POST
        self.object.is_staff = "is_staff" in request.POST

        self.object.user_permissions.set(
            request.POST.getlist("permissions")
        )

        self.object.save(
            update_fields=[
                "is_active",
                "is_staff",
            ]
        )

        messages.success(
            request,
            _("User permissions updated successfully.")
        )

        return redirect("accounts:user_list")


class AccountUpdateView(DashboardBaseMixin, UpdateView):
    model = User
    form_class = AccountUpdateForm
    template_name = "accounts/account.html"
    context_object_name = "user_obj"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("My Account")
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            _("Your account has been updated successfully.")
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:account")


class AccountPasswordView(DashboardBaseMixin, FormView):
    template_name = "accounts/password.html"
    form_class = AccountPasswordChangeForm
    success_url = reverse_lazy("accounts:account")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()

        update_session_auth_hash(
            self.request,
            user
        )

        messages.success(
            self.request,
            _("Your password has been changed successfully.")
        )

        return super().form_valid(form)