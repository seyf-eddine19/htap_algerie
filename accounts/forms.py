from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "dashboard-input",
            })


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "dashboard-input",
            })


class PermissionField(forms.ModelMultipleChoiceField):
    """عرض الصلاحيات المترجمة لتطبيقات محددة فقط."""

    PERMISSION_TRANSLATIONS = {
        "add": _("Add"),
        "change": _("Change"),
        "delete": _("Delete"),
        "view": _("View"),
    }

    def __init__(self, *args, **kwargs):
        target_apps = [
            "core",
            "articles",
            "activities",
        ]

        queryset = (
            Permission.objects
            .filter(
                content_type__app_label__in=target_apps
            )
            .select_related("content_type")
            .order_by(
                "content_type__app_label",
                "content_type__model",
                "codename",
            )
        )

        kwargs["queryset"] = queryset
        kwargs["widget"] = forms.CheckboxSelectMultiple()

        super().__init__(*args, **kwargs)

    def label_from_instance(self, permission):
        app_label = permission.content_type.app_label
        model_name = permission.content_type.model

        action = permission.codename.split("_")[0]

        action_label = self.PERMISSION_TRANSLATIONS.get(
            action,
            action
        )

        try:
            model_class = apps.get_model(
                app_label,
                model_name
            )

            model_label = model_class._meta.verbose_name_plural

        except (LookupError, AttributeError):
            model_label = model_name

        return f"{action_label} {model_label}"


class UserPermissionsForm(forms.ModelForm):
    permissions = PermissionField(
        label=_("Permissions"),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "is_active",
            "is_staff",
            "permissions",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields["permissions"].initial = (
                self.instance.user_permissions.values_list(
                    "id",
                    flat=True,
                )
            )

    @property
    def grouped_permissions(self):
        groups = {}

        permission_field = self.fields["permissions"]

        for permission in permission_field.queryset:
            app_label = permission.content_type.app_label

            if app_label not in groups:
                groups[app_label] = []

            groups[app_label].append({
                "permission": permission,
                "label": permission_field.label_from_instance(permission),
            })

        return groups.items()

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            self.save_m2m()

        return user

    def save_m2m(self):
        self.instance.user_permissions.set(
            self.cleaned_data.get("permissions", [])
        )


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "dashboard-input",
            })


class AccountPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "dashboard-input",
            })