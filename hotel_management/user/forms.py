from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AuthUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re
from datetime import date

class AuthUserCreationForm(UserCreationForm):
    
    def clean(self, *args, **kwargs):
        print("runnnig")
        cleaned_data = super(AuthUserCreationForm,self).clean(*args, **kwargs)
        
        try:
            phone_number = cleaned_data['phone_number']
            age = cleaned_data['age']
        except KeyError:
            raise ValidationError('')

        if (age < 18 or age > 120 ):
            raise ValidationError(
               _('Cannot create user for this age.')
            )

        exp_match = re.match(r"^\d{10}$", phone_number)

        if (exp_match is None):
            raise ValidationError(
               _('Invalid Phone Number.')
            )

        return cleaned_data


class AuthUserChangeForm(UserChangeForm):
    
    def clean(self, *args, **kwargs):
        cleaned_data = super(AuthUserChangeForm,self).clean(*args, **kwargs)

        try:
            phone_number = cleaned_data['phone_number']
            age = cleaned_data['age']
        except KeyError:
            raise ValidationError('')

        if (age < 18 or age > 120 ):
            raise ValidationError(
               _('Cannot create user for this age.')
            )

        exp_match = re.match(r"^\d{10}$", phone_number)

        if (exp_match is None):
            raise ValidationError(
               _('Invalid Phone Number.')
            )

        return cleaned_data


