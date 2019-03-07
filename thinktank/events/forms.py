from django import forms
from .models import Event, EventPhoto, EventVideo


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'venue', 'when_date', 'when_time')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'when_date': DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYY'}),
            'when_time': TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM AM/PM'}),
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
