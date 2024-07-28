from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext ,  gettext_lazy as _



widget_attrs = {'class': 'form-control '}
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


class LoginForm(AuthenticationForm):
    
    uname_att = {'autofocus' : True, 'class' : 'form-control'}
    username = UsernameField(widget=forms.TextInput(attrs=uname_att))
    
    upass_att = {'autocomplete' : 'current-password', 'class': 'form-control ' }
    password = forms.CharField(label=_("Password"), strip=False, widget = forms.PasswordInput(attrs= upass_att))