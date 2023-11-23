from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'body', 'category', 'image']
