from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Activity, ActivityTranslation, ActivityBlock, ActivityImage


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            "activity_type",
            "status",
            "featured_image",
            "location",
            "start_date",
            "end_date",
            "is_featured",
        ]
        widgets = {
            "activity_type": forms.Select(attrs={
                "class": "form-input",
            }),
            "status": forms.Select(attrs={
                "class": "form-input",
            }),
            "featured_image": forms.ClearableFileInput(attrs={
                "class": "form-file",
                "accept": "image/*",
            }),
            "location": forms.TextInput(attrs={
                "class": "form-input",
            }),
            "start_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-input",
                    "type": "datetime-local",
                },
            ),
            "end_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-input",
                    "type": "datetime-local",
                },
            ),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "form-checkbox",
            }),
        }


class ActivityTranslationForm(forms.ModelForm):
    class Meta:
        model = ActivityTranslation
        fields = [
            "language",
            "title",
            "excerpt",
            "meta_title",
            "meta_description",
        ]
        widgets = {
            "language": forms.Select(attrs={
                "class": "form-input",
            }),
            "title": forms.TextInput(attrs={
                "class": "form-input",
            }),
            "excerpt": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 4,
            }),
            "meta_title": forms.TextInput(attrs={
                "class": "form-input",
            }),
            "meta_description": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 3,
            }),
        }


class ActivityBlockForm(forms.ModelForm):
    class Meta:
        model = ActivityBlock
        fields = [
            "translation",
            "block_type",
            "order",
            "title",
            "text",
            "image",
            "image_caption",
        ]
        widgets = {
            "translation": forms.HiddenInput(),
            "block_type": forms.Select(attrs={
                "class": "form-input",
            }),
            "order": forms.NumberInput(attrs={
                "class": "form-input",
                "min": 0,
            }),
            "title": forms.TextInput(attrs={
                "class": "form-input",
            }),
            "text": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 5,
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-file",
                "accept": "image/*",
            }),
            "image_caption": forms.TextInput(attrs={
                "class": "form-input",
            }),
        }


class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = [
            "image",
            "caption",
            "order",
        ]
        widgets = {
            "image": forms.ClearableFileInput(attrs={
                "class": "form-file",
                "accept": "image/*",
            }),
            "caption": forms.TextInput(attrs={
                "class": "form-input",
            }),
            "order": forms.NumberInput(attrs={
                "class": "form-input",
                "min": 0,
            }),
        }


ActivityTranslationFormSet = inlineformset_factory(
    Activity,
    ActivityTranslation,
    form=ActivityTranslationForm,
    extra=3,
    max_num=3,
    validate_max=True,
    can_delete=True,
)

ActivityImageFormSet = inlineformset_factory(
    Activity,
    ActivityImage,
    form=ActivityImageForm,
    extra=1,
    can_delete=True,
)