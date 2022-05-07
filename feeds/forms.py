from django import forms
from .models import Comment
# from .forms import EmailPostForm, CommentForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')