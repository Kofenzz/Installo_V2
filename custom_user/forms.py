from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from custom_user.models import User, Profile


#
# class AuthenticationNewForm(AuthenticationForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.fields['username'].widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Please enter your username'})
#         self.fields['password'].widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Please enter your password'})
#

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'phone_number',
                  'password1', 'password2', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Type your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Retype your password'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Enter your last name', 'style': 'width:100%'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Enter your first name", 'style': 'width:100%'
        })
        (self.fields['email'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Enter your email address'
        }),
         self.fields['phone_number'].widget.attrs.update({
             'class': 'form-control', 'placeholder': 'Enter your phone number'
         }))


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email', 'style': 'width:100%'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'phone_number', 'address_1', 'address_2', 'user_type')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'First Name', 'style': 'width:100%'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Last Name', 'style': 'width:100%'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Phone Number',
                       'style': 'width:100%'}),
            'address_1': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'First address line',
                       'style': 'width:100%'}),
            'address_2': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Second address line',
                       'style': 'width:100%'}),
            'user_type': forms.Select(attrs={'class': 'form-control ', 'style': 'width:100%'})
        }
