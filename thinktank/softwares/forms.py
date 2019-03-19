from django import forms
from .models import (Software, Configuration, WorkingProject, Technology,)


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class WorkingProjectForm(forms.ModelForm):
    class Meta:
        model = WorkingProject
        fields = ('title', 'description', 'tech_used')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tech_used': forms.TextInput(attrs={'class': 'form-control'})
        }


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
