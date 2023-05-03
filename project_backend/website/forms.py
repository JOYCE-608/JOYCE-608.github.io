from django import forms

from .models  import Comment

class CommentForm(forms.ModelForm):
    comment = forms.TextInput()

    class Meta:
        model = Comment
        exclude = ("time", )