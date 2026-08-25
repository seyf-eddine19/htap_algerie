from django import forms 
from .models import Member, ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("first_name", "last_name", "email", "phone", "wilaya", "subject", "message","consent")


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "name_ar", "role_ar", "role_en", "role_fr", "photo", "bio", "order", "is_active")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-input'}),
            'role_ar': forms.TextInput(attrs={'class': 'form-input'}),
            'role_en': forms.TextInput(attrs={'class': 'form-input'}),
            'role_fr': forms.TextInput(attrs={'class': 'form-input'}),
            'bio': forms.TextInput(attrs={'class': 'form-input'}),
        }