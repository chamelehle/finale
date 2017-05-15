from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import submit, fact, aboutl
from django.core.validators import validate_slug

def verify_comments(value):
        return value

class SubmitForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Name:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='Date:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter date of event'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Description:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
class FactForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Title:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='URL:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter url source'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Description:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
class AboutForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Name:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='Email:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter url source'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Position:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
    phone_num = forms.CharField(
        label='Phone:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter phone #'
            }))

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name':'username'
        })
    )
    password=forms.CharField(
        label="password",
        max_length=32,
        widget=forms.PasswordInput()
    )
class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
