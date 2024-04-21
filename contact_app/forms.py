from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control','id':'id-name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','id':'id-email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'id-subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control md-textarea', 'rows' : '3', 'id':'id-message'}))