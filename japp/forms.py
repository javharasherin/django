from django import forms
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=['first_name','last_name','email','address']