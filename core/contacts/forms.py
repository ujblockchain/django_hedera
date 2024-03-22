from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    reference = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'cols': '30',
                'rows': '7'
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'subject',
            'reference',
            'message',
        ]
