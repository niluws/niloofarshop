from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'id':"name" ,'placeholder':"Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control", 'id':"email" ,'placeholder':"Your Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'id':"subject" ,'placeholder':"Subject"}))
    message = forms.CharField(widget=forms.Textarea( attrs={'class':"form-control", 'id':"message" ,'placeholder':"Message"}))