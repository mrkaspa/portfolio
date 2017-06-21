from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False, label="Your email")
    message = forms.CharField()
