from django import forms
from .models import ClientMessage

class messageform(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'first_name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder': 'Your name',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'last_name', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
            'placeholder': 'Your surname',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id': 'email_address', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
            'placeholder': 'Email',
        }
    ))
    message = forms.CharField(max_length=100000000, widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'id': 'message', 
            'type': 'text',
            'name': 'message',
            'data-constraints': '@Required',
            'placeholder': 'Message',
            'row':'5',
        }
    ))
    class Meta:
        model = ClientMessage
        fields = '__all__'