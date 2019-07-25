from django import forms

from django.utils.translation import ugettext_lazy as _

# Copyright Videntity Systems Inc.


class MFACodeForm(forms.Form):
    code = forms.CharField(widget=forms.PasswordInput, max_length=30,
                           label=_('Code*'))
    required_css_class = 'required'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label=_('User'),
                               widget=forms.TextInput(attrs={'placeholder': 'Your username*'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password*'}), max_length=150,
                               label=_('Your Password*'))
    required_css_class = 'required'

    def clean_username(self):
        return self.cleaned_data.get("username", "").strip().lower()
