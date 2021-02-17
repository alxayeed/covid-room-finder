from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
import re


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password(self):
        "Check Password Validation"
        password = self.cleaned_data['password']

        def validate_password(password):
            errors = []

            if len(password) < 6:
                errors.append(ValidationError(
                    'Password must be at least 6 characters'
                ))

            if (bool(re.match('^\w*$', password)) == True):
                errors.append(ValidationError(
                    'Password must contain at least one special character'
                ))

            if errors:
                raise ValidationError(errors)

        validate_password(password)
        return password
