from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.forms import TextInput
import random

from custom_user.models import User

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
                  'password1','password2',]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Type your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Retype your password'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Enter your last name'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Enter your first name"
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
            {'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})



