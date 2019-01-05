from django import forms

from .models import Forum, Comment, CommentOnComment


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('q_title', 'detail', 'tag',)

        widgets = {
            'q_title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}


class CommentOnCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnComment
        fields = ('text', )

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}
