from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Activity, ActivityTranslation, ActivityBlock, ActivityImage

# --- Modern Tailwind Utility Classes ---
INPUT_CLASS = (
    "w-full rounded-xl border border-slate-200 dark:border-slate-800 "
    "bg-white dark:bg-slate-900/60 px-3.5 py-2.5 text-sm font-medium "
    "text-slate-900 dark:text-slate-100 placeholder:text-slate-400 "
    "focus:border-purple-500 focus:outline-none focus:ring-4 focus:ring-purple-500/10 "
    "dark:focus:border-purple-400 dark:focus:ring-purple-400/10 transition"
)

FILE_CLASS = (
    "w-full text-sm text-slate-500 dark:text-slate-400 "
    "file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 "
    "file:text-xs file:font-semibold file:bg-purple-50 file:text-purple-700 "
    "hover:file:bg-purple-100 dark:file:bg-purple-950/50 dark:file:text-purple-300 "
    "file:transition cursor-pointer"
)

CHECKBOX_CLASS = (
    "h-4 w-4 rounded-md border-slate-300 dark:border-slate-700 "
    "text-purple-600 focus:ring-purple-500/20 dark:bg-slate-900 transition"
)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            "activity_type", "status", "featured_image", 
            "location", "start_date", "end_date", "is_featured"
        ]
        widgets = {
            "activity_type": forms.Select(attrs={"class": INPUT_CLASS}),
            "status": forms.Select(attrs={"class": INPUT_CLASS}),
            "featured_image": forms.ClearableFileInput(attrs={"class": FILE_CLASS, "accept": "image/*"}),
            "location": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("e.g. Main Auditorium / Remote")}),
            "start_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"class": INPUT_CLASS, "type": "datetime-local"},
            ),
            "end_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"class": INPUT_CLASS, "type": "datetime-local"},
            ),
            "is_featured": forms.CheckboxInput(attrs={"class": CHECKBOX_CLASS}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if start and end and end < start:
            raise ValidationError(_("End date cannot be prior to start date."))
        return cleaned_data


class ActivityTranslationForm(forms.ModelForm):
    class Meta:
        model = ActivityTranslation
        fields = ["language", "title", "excerpt", "meta_title", "meta_description"]
        widgets = {
            "language": forms.HiddenInput(),
            "title": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("Enter title...")}),
            "excerpt": forms.Textarea(attrs={"class": INPUT_CLASS, "rows": 3, "placeholder": _("Brief summary of the activity...")}),
            "meta_title": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("SEO Title (Optional)")}),
            "meta_description": forms.Textarea(attrs={"class": INPUT_CLASS, "rows": 2, "placeholder": _("SEO Description (Optional)")}),
        }


class ActivityBlockForm(forms.ModelForm):
    class Meta:
        model = ActivityBlock
        fields = ["translation", "block_type", "order", "title", "text", "image", "image_caption"]
        widgets = {
            "translation": forms.HiddenInput(),
            "block_type": forms.Select(attrs={"class": INPUT_CLASS}),
            "order": forms.NumberInput(attrs={"class": INPUT_CLASS, "min": 0}),
            "title": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("Block Header")}),
            "text": forms.Textarea(attrs={"class": INPUT_CLASS, "rows": 4, "placeholder": _("Write body content...")}),
            "image": forms.ClearableFileInput(attrs={"class": FILE_CLASS, "accept": "image/*"}),
            "image_caption": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("Image Caption")}),
        }


class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = ["image", "caption", "order"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": FILE_CLASS, "accept": "image/*"}),
            "caption": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": _("Caption text")}),
            "order": forms.NumberInput(attrs={"class": INPUT_CLASS, "min": 0}),
        }


# Formsets
ActivityTranslationFormSet = inlineformset_factory(
    Activity,
    ActivityTranslation,
    form=ActivityTranslationForm,
    extra=0,
    can_delete=False,
)

ActivityImageFormSet = inlineformset_factory(
    Activity,
    ActivityImage,
    form=ActivityImageForm,
    extra=1,
    can_delete=True,
)