# coding: utf-8
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    '''
    A form that creates a user, with no privileges, from the given username and password.
    '''
    error_message ={
        'duplicate_username': ("The user with this name exists."),
        'password_mismatch': ("Passwords are not the same.")
    }
    username = forms.CharField(max_length=30, label="User Name")
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_message['duplicate_username'])

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(self.error_message['password_mismatch'])
        return password2


