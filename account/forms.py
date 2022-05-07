from django import forms
# from .models import Comment
# from .forms import EmailPostForm, CommentForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

