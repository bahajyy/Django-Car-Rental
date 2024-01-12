# forms.py

from django import forms
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'country', 'city']
        widgets = {
            'password': forms.PasswordInput(),
        }
