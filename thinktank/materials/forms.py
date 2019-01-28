from django import forms
from .models import Material, MaterialImage, MaterialLink, MaterialDocument, MaterialVideo


class CreateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'You can leave it empty'}),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = MaterialDocument
        fields = ('document',)


class LinkForm(forms.ModelForm):
    class Meta:
        model = MaterialLink
        fields = ('link',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = MaterialImage
        fields = ('image',)


class VideoForm(forms.ModelForm):
    class Meta:
        model = MaterialVideo
        fields = ('video',)
