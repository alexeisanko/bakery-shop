from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from . import models


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = models.BakeryUser
        fields = ('username',)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
            if self.errors:
                raise ValidationError(self.errors)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


    
