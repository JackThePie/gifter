from django import forms
from .models import Gift
class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)


# class ContactForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'onchange': 'this.form.submit();', 'class': 'editinput'}))
#     class Meta:
#         model = Gift
#         fields = ('email',)