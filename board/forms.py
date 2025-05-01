from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Posts, Responses


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['category', 'heading', 'text']


class ResponsesForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['text',]


class ResponsesStatusForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['status',]
