from django import forms
from .models import Customer
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean(self, *args, **kwargs):
        cleaned_data = super(CustomerForm,self).clean(*args, **kwargs)
        
        try:
            zip_code = cleaned_data['zip_code']
        except KeyError:
            raise ValidationError('')

        exp_match = re.match(r"^\d{6}$", zip_code)

        if (exp_match is None):
            raise ValidationError(
               _('Invalid ZIP code.')
            )

        return cleaned_data
