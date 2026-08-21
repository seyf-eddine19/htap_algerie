from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Article, ArticleTranslation, ArticleBlock


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "slug", "category", "featured_image", "author", "status", "is_featured"
        ]
        widgets = {
            "slug": forms.Select(attrs={"class": "form-input"}),
            "category": forms.Select(attrs={"class": "form-input"}),
            "featured_image": forms.ClearableFileInput(attrs={"class": "form-file", "accept": "image/*"}),
            "author": forms.TextInput(attrs={"class": "form-input"}),
            "status": forms.Select(attrs={"class": "form-input"}),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class ArticleTranslationForm(forms.ModelForm):
    class Meta:
        model = ArticleTranslation
        fields = [
            "language", "title", "excerpt", "meta_title", "meta_description"
        ]
        widgets = {
            "language": forms.Select(attrs={"class": "form-input"}),
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "excerpt": forms.Textarea(attrs={"class": "form-input", "rows": 4}),
            "meta_title": forms.TextInput(attrs={"class": "form-input"}),
            "meta_description": forms.Textarea(attrs={"class": "form-input","rows": 3}),
        }

class ArticleBlockForm(forms.ModelForm):
    class Meta:
        model = ArticleBlock
        fields = [ 
            "block_type", "order", "title", "text", "caption", "image", "document", "url"
        ]

        widgets = {
            "block_type": forms.Select(attrs={
                "class": "block-type-input w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition",
            }),

            "order": forms.NumberInput(attrs={
                "class": "w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition",
                "min": "0",
            }),

            "title": forms.TextInput(attrs={
                "class": "w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition",
                "maxlength": "250",
            }),

            "text": forms.Textarea(attrs={
                "class": "w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition resize-y",
                "rows": "6",
            }),

            "caption": forms.TextInput(attrs={
                "class": "w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition",
                "maxlength": "300",
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-slate-600 dark:text-slate-300 file:me-4 file:py-2.5 file:px-4 file:rounded-lg file:border-0 file:bg-purple-50 file:text-purple-700 dark:file:bg-purple-900/30 dark:file:text-purple-300 hover:file:bg-purple-100 transition",
                "accept": "image/jpeg,image/png,image/webp",
            }),

            "document": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-slate-600 dark:text-slate-300 file:me-4 file:py-2.5 file:px-4 file:rounded-lg file:border-0 file:bg-purple-50 file:text-purple-700 dark:file:bg-purple-900/30 dark:file:text-purple-300 hover:file:bg-purple-100 transition",
                "accept": ".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx",
            }),

            "url": forms.URLInput(attrs={
                "class": "w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:border-purple-600 focus:ring-2 focus:ring-purple-600/20 outline-none transition",
                "placeholder": "https://",
            }),
        }

        labels = {
            "block_type": _("Block Type"),
            "order": _("Order"),
            "title": _("Title"),
            "text": _("Text"),
            "caption": _("Caption"),
            "image": _("Image"),
            "document": _("Document"),
            "url": _("URL"),
        }

        help_texts = {
            "title": _("Optional title for this block."),
            "text": _("Content text for this block."),
            "caption": _("Optional caption or description."),
            "url": _("URL used by video, embed or button blocks."),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["order"].required = True

        self.fields["title"].required = False
        self.fields["text"].required = False
        self.fields["caption"].required = False
        self.fields["image"].required = False
        self.fields["document"].required = False
        self.fields["url"].required = False

    def clean(self):
        cleaned_data = super().clean()

        block_type = cleaned_data.get("block_type")
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        caption = cleaned_data.get("caption")
        image = cleaned_data.get("image")
        document = cleaned_data.get("document")
        url = cleaned_data.get("url")

        if not block_type:
            return cleaned_data

        # ==========================================
        # HEADING
        # ==========================================
        if block_type == ArticleBlock.BlockType.HEADING:
            if not title:
                self.add_error(
                    "title",
                    _("Heading text is required.")
                )

        # ==========================================
        # PARAGRAPH
        # ==========================================
        elif block_type == ArticleBlock.BlockType.PARAGRAPH:
            if not text:
                self.add_error(
                    "text",
                    _("Paragraph text is required.")
                )

        # ==========================================
        # QUOTE
        # ==========================================
        elif block_type == ArticleBlock.BlockType.QUOTE:
            if not text:
                self.add_error(
                    "text",
                    _("Quote text is required.")
                )

        # ==========================================
        # CALLOUT
        # ==========================================
        elif block_type == ArticleBlock.BlockType.CALLOUT:
            if not title:
                self.add_error(
                    "title",
                    _("Callout title is required.")
                )

            if not text:
                self.add_error(
                    "text",
                    _("Callout text is required.")
                )

        # ==========================================
        # DIVIDER
        # ==========================================
        elif block_type == ArticleBlock.BlockType.DIVIDER:
            pass

        # ==========================================
        # IMAGE
        # ==========================================
        elif block_type == ArticleBlock.BlockType.IMAGE:
            if not image and not self.instance.image:
                self.add_error(
                    "image",
                    _("Please select an image.")
                )

        # ==========================================
        # VIDEO
        # ==========================================
        elif block_type == ArticleBlock.BlockType.VIDEO:
            if not url:
                self.add_error(
                    "url",
                    _("Video URL is required.")
                )
            elif not self._is_video_url(url):
                self.add_error(
                    "url",
                    _("Please enter a valid YouTube or Vimeo URL.")
                )

        # ==========================================
        # DOCUMENT
        # ==========================================
        elif block_type == ArticleBlock.BlockType.DOCUMENT:
            if not document and not self.instance.document:
                self.add_error(
                    "document",
                    _("Please select a document.")
                )

        # ==========================================
        # EMBED
        # ==========================================
        elif block_type == ArticleBlock.BlockType.EMBED:
            if not url:
                self.add_error(
                    "url",
                    _("Embed URL is required.")
                )

        # ==========================================
        # BUTTON
        # ==========================================
        elif block_type == ArticleBlock.BlockType.BUTTON:
            if not title:
                self.add_error(
                    "title",
                    _("Button text is required.")
                )

            if not url:
                self.add_error(
                    "url",
                    _("Button URL is required.")
                )

        return cleaned_data

    @staticmethod
    def _is_video_url(url):
        if not url:
            return False

        allowed_domains = (
            "youtube.com",
            "www.youtube.com",
            "youtu.be",
            "vimeo.com",
            "www.vimeo.com",
        )

        return any(domain in url.lower() for domain in allowed_domains)



class ArticleBlockForm(forms.ModelForm):
    class Meta:
        model = ArticleBlock
        fields = [
            "block_type",
            "order",
            "title",
            "text",
            "caption",
            "image",
            "document",
            "url",
        ]

        widgets = {
            "block_type": forms.Select(attrs={
                "class": "block-type-select w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-purple-500",
            }),
            "order": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white",
                "min": "0",
            }),
            "title": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white",
                "maxlength": "250",
                "placeholder": _("Enter title..."),
            }),
            "text": forms.Textarea(attrs={
                "class": "w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white resize-y",
                "rows": "6",
                "maxlength": "5000",
                "placeholder": _("Enter content..."),
            }),
            "caption": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white",
                "maxlength": "300",
                "placeholder": _("Enter caption..."),
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-slate-600 dark:text-slate-300",
                "accept": "image/jpeg,image/png,image/webp,image/gif",
            }),
            "document": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-slate-600 dark:text-slate-300",
                "accept": ".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx",
            }),
            "url": forms.URLInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-4 py-3 text-sm text-slate-900 dark:text-white",
                "maxlength": "500",
                "placeholder": "https://...",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].label = _("Title")
        self.fields["text"].label = _("Text")
        self.fields["caption"].label = _("Caption")
        self.fields["image"].label = _("Image")
        self.fields["document"].label = _("Document")
        self.fields["url"].label = _("URL")

        self.fields["title"].help_text = _("Maximum 250 characters.")
        self.fields["text"].help_text = _("Maximum 5,000 characters.")
        self.fields["caption"].help_text = _("Maximum 300 characters.")
        self.fields["url"].help_text = _("Enter a valid URL.")

    def clean(self):
        cleaned_data = super().clean()

        block_type = cleaned_data.get("block_type")
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        caption = cleaned_data.get("caption")
        image = cleaned_data.get("image")
        document = cleaned_data.get("document")
        url = cleaned_data.get("url")

        if block_type == ArticleBlock.BlockType.HEADING:
            if not title:
                self.add_error("title", _("A heading is required."))

            if title and len(title) > 250:
                self.add_error("title", _("Heading cannot exceed 250 characters."))

        elif block_type == ArticleBlock.BlockType.PARAGRAPH:
            if not text:
                self.add_error("text", _("Paragraph content is required."))

        elif block_type == ArticleBlock.BlockType.QUOTE:
            if not text:
                self.add_error("text", _("Quote text is required."))

            if len(text or "") > 2000:
                self.add_error("text", _("Quote cannot exceed 2,000 characters."))

        elif block_type == ArticleBlock.BlockType.CALLOUT:
            if not text:
                self.add_error("text", _("Callout content is required."))

            if len(text or "") > 2000:
                self.add_error("text", _("Callout cannot exceed 2,000 characters."))

        elif block_type == ArticleBlock.BlockType.DIVIDER:
            cleaned_data["title"] = ""
            cleaned_data["text"] = ""
            cleaned_data["caption"] = ""
            cleaned_data["image"] = None
            cleaned_data["document"] = None
            cleaned_data["url"] = ""

        elif block_type == ArticleBlock.BlockType.IMAGE:
            if not image and not self.instance.image:
                self.add_error("image", _("An image is required."))

            if caption and len(caption) > 300:
                self.add_error("caption", _("Caption cannot exceed 300 characters."))

        elif block_type == ArticleBlock.BlockType.VIDEO:
            if not url:
                self.add_error("url", _("A video URL is required."))

            if caption and len(caption) > 300:
                self.add_error("caption", _("Caption cannot exceed 300 characters."))

        elif block_type == ArticleBlock.BlockType.DOCUMENT:
            if not document and not self.instance.document:
                self.add_error("document", _("A document is required."))

            if caption and len(caption) > 300:
                self.add_error("caption", _("Caption cannot exceed 300 characters."))

        elif block_type == ArticleBlock.BlockType.EMBED:
            if not url:
                self.add_error("url", _("An embed URL is required."))

            if len(url or "") > 500:
                self.add_error("url", _("URL cannot exceed 500 characters."))

        elif block_type == ArticleBlock.BlockType.BUTTON:
            if not title:
                self.add_error("title", _("Button text is required."))

            if not url:
                self.add_error("url", _("Button URL is required."))

            if title and len(title) > 100:
                self.add_error("title", _("Button text cannot exceed 100 characters."))

        return cleaned_data
ArticleBlockFormSet = inlineformset_factory(
    ArticleTranslation, ArticleBlock, form=ArticleBlockForm, extra=3, max_num=3, validate_max=True, can_delete=True,
)

ArticleTranslationFormSet = inlineformset_factory(
    Article, ArticleTranslation, form=ArticleTranslationForm, extra=3, max_num=3, validate_max=True, can_delete=True,
)





from django import forms
from django.forms import inlineformset_factory
from .models import Article, ArticleTranslation, ArticleBlock, Language

class ArticleForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Article
        fields = ['category', 'author', 'featured_image', 'status', 'is_featured', 'published_at']

    def clean(self):
        cleaned_data = super().clean()
        pub_date = self.cleaned_data.get('pub_date')
        if pub_date:
            cleaned_data['published_at'] = pub_date
        return cleaned_data


class ArticleTranslationForm(forms.ModelForm):
    class Meta:
        model = ArticleTranslation
        fields = ['language', 'title', 'excerpt', 'meta_title', 'meta_description']
        widgets = {
            'meta_title': forms.TextInput(attrs={'class': 'dashboard-input'}),
            'meta_description': forms.TextInput(attrs={'class': 'dashboard-input'}),
        }


# Base formset factory for translations (Arabic, English, French)
ArticleTranslationFormSet = inlineformset_factory(
    Article,
    ArticleTranslation,
    form=ArticleTranslationForm,
    extra=0,
    can_delete=False,
    min_num=3,
    max_num=3,
)

class ArticleBlockForm(forms.ModelForm):
    class Meta:
        model = ArticleBlock
        fields = [
            'block_type', 'order', 'title', 'text', 'caption', 
            'image', 'document', 'url', 'heading_level', 'callout_style'
        ]


ArticleBlockFormSet = inlineformset_factory(
    ArticleTranslation,
    ArticleBlock,
    form=ArticleBlockForm,
    extra=0,
    can_delete=True
)