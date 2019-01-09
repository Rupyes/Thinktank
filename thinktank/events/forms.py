from django import forms
from .models import Event, EventPhoto, EventVideo


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'video', 'venue')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    photo = forms.ImageField(label='Image')

    class Meta:
        model = EventPhoto
        fields = ('photo', )


class VideoForm(forms.ModelForm):
    video = forms.FileField(label='Video')

    class Meta:
        model = EventVideo
        fields = ('video',)
