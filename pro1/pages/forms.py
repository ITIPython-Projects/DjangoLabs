from django import forms
from .models import UserData


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
