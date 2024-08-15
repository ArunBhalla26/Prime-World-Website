from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField ,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext ,  gettext_lazy as _
from django.contrib.auth import password_validation
from.models import Customer



widget_attrs = {'class': 'form-control '}
class CustomerRegistrationForm(UserCreationForm):

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


class ProfileForm (forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode' ]
        widgets = { "name":  forms.TextInput(attrs=widget_attrs),
                   "locality" : forms.TextInput(attrs=widget_attrs), 
                   "city" : forms.TextInput(attrs=widget_attrs), 
                   "state" : forms.Select(attrs=widget_attrs), 
                   "zipcode" : forms.NumberInput(attrs=widget_attrs), 
                   }
        labels = {
            "name": "Full Name",
            "locality": "Locality",
            "city": "City",
            "state": "State",
            "zipcode": "Zip Code",
        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = "Old Password", widget = forms.PasswordInput(attrs=widget_attrs))
    new_password1 = forms.CharField(label="New Password" , widget = forms.PasswordInput(attrs=widget_attrs), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label="Confirm Password" , widget = forms.PasswordInput(attrs=widget_attrs))
    

