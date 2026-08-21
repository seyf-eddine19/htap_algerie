from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

# ============================================================
# BASE DASHBOARD MIXIN
# ============================================================

class DashboardAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Allows only authenticated staff users to access the dashboard.
    """

    login_url = "accounts:login"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect("core:home")


class DashboardPermissionMixin(DashboardAccessMixin, PermissionRequiredMixin):
    """
    Dashboard access plus a specific Django permission.
    """
    raise_exception = True


class DashboardBaseMixin(DashboardAccessMixin):
    """
    Common configuration for dashboard views.
    """

    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dashboard"] = True
        return context
