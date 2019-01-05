from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ContactUsForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100, help_text='100 characters max.', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    detail = forms.CharField(label='Detail', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
