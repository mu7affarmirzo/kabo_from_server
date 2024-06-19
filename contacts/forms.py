from django import forms
from contacts.models import ContactUsModel


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUsModel
        fields = [
            'full_name',
            'message',
            'phone_number',
            'email',
        ]