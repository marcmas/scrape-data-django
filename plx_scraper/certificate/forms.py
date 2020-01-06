import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms
from .models import Certificate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create a form for edit path
class CertificateModelForm(forms.ModelForm):
    leave_date = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker', 'placeholder': 'Data wyjścia'}), label='Data wyjścia')
    leave_hour = forms.TimeField(widget=forms.TextInput(attrs={'id':'timepicker', 'placeholder': 'Godzina wyjścia'}), label='Godzina wyjścia')
    return_hour = forms.TimeField(widget=forms.TextInput(attrs={'id':'timepicker1', 'placeholder': 'Godzina Przyjścia'}), label='Godzina przyjścia', required=False)

    class Meta:
        model = Certificate
        fields = ['leave_date', 'leave_hour', 'return_hour']


    def clean_leave_date(self):
        data = self.cleaned_data['leave_date']

        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Nieprawidłowa data z przeszłości'))

        return data

