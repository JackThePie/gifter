from django import forms

class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)
    name = forms.CharField(label="LOLOLO", max_length=100)