from django import forms
from .models import Category, Page, UserProfile
# from django.forms import ModelForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', ]


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        exclude = ['category', ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website',)
