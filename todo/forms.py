from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo_User, Todo


class Signin_Form(AuthenticationForm):
    field_order = ['username', 'password']
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'username',
               'name': "username",
               'placeholder': "Username",
               }), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'type': 'password',
               'name': "password",
               'placeholder': "Password",
               }), label='')


class Signup_Form(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'first_name',
               'name': "first_name",
               'placeholder': "First Name",
               }), label='')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'last_name',
               'name': "last_name",
               'placeholder': "Last Name",
               }), label='')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'type': 'email',
               'name': "email",
               'placeholder': "Email",
               }), label='')
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'username',
               'name': "username",
               'placeholder': "Username",
               }), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'type': 'password',
               'name': "password",
               'placeholder': "Password",
               }), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'type': 'password',
               'name': "password",
               'placeholder': "Confirm Password",
               }), label='')

    field_order = [
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
    ]

    class Meta:
        model = Todo_User
        fields = {
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        }


class Create_Todo_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'name',
               'name': "name",
               'placeholder': "Name",
               }), label='')
    due = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control',
               'type': 'date',
               'name': "due",
               'placeholder': "Due",
               }), label='')

    memo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'text',
               'name': "memo",
               'placeholder': "Memo",
               }), label='')

    field_order = [
        'name',
        'memo',
        'important',
        'urgent',
        'due', ]

    class Meta:
        model = Todo
        fields = {
            'name',
            'memo',
            'important',
            'urgent',
            'due',
        }
