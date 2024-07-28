from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
widget_attrs = {'class': 'form-control'}
class CustomerRegistrationForm(UserCreationForm):
    # Define common widget attributes
    
    
    # The 'password1' and 'password2' fields are part of UserCreationForm
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=widget_attrs)
    )
    
    password2 = forms.CharField(
        label='Confirm Password (again)',
        widget=forms.PasswordInput(attrs=widget_attrs)
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs=widget_attrs)
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs=widget_attrs )
        }
