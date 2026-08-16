from django.forms import ModelForm
from .models import ContactMessage

class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("first_name", "last_name", "email", "phone", "subject", "message")