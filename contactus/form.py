from .models import contactus
from django import forms

class contactform(forms.ModelForm):
    class Meta:
        model = contactus
        fields = '__all__'
