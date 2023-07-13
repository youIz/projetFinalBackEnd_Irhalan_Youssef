
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'img_url', 'newsletter')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'img_url': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Image URL'}),
            'newsletter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


