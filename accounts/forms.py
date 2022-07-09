from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"example@gmail.com",'class':'form-control'}),validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ])
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"password",'class':'form-control'}),validators=[
            validators.MaxLengthValidator(100),
        ])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"confirm password",'class':'form-control'}),validators=[
            validators.MaxLengthValidator(100),
        ])
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password'),
        confirm_password = self.cleaned_data.get('confirm_password'),
        if password == confirm_password:
            return confirm_password
        raise ValidationError('you should enter both password same ')

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"example@gmail.com",'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"password",'class':'form-control'}))
