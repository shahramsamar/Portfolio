from django import forms
from website.models import ContactModel


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = '__all__'
        
    