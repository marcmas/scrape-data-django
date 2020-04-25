from django import forms
from .models import Path


# Create a form for edit path
class PathModelForm(forms.ModelForm):
    path = forms.CharField(widget=forms.TextInput())
    
    class Meta:
        model = Path
        fields = ['path']