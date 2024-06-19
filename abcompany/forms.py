from django import forms
from abcompany.models import SendResumeModel


class SendResumeForm(forms.ModelForm):
    # cv = forms.FileField(
    #     label='Select a file',
    #     help_text='max. 42 megabytes'
    # )

    class Meta:
        model = SendResumeModel
        fields = [
            'full_name',
            'message',
            'phone_number',
            'email',
            'cv',
        ]
