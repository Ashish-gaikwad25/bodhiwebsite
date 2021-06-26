
from django import forms



class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),label='Your Name',max_length=50,min_length=4,required=True)  
   
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label='Your Email',max_length=50,min_length=8, required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),label='Subject',max_length=50,required=True)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}),label='Message',max_length=200,min_length=10,required=True)
    
