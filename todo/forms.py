from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Todo_User, Todo


class Signup_Form(UserCreationForm):
    field_order = ['first_name',
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
    name = forms.CharField(max_length=50)
    memo = forms.TextInput()
    important = forms.BooleanField()
    warning = forms.DateInput()
    field_order = ['name',
            'memo',
            'important',
            'warning',]
    class Meta:
        model = Todo
        fields = {
            'name',
            'memo',
            'important',
            'warning',
        }
