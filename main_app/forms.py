from django import forms
from .models import Gift
# class ContactForm(forms.Form):
#     contact_email = forms.EmailField(required=True)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ('email',)