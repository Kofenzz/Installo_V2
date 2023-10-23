from django import forms

from adress.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'address_name': forms.TextInput(attrs={'class': 'form-control', 'style':'width:100%'}),
            'recipient_name': forms.TextInput(attrs={'class': 'form-control', 'style':'width:100%'}),
            'street_address1': forms.TextInput(attrs={'class': 'form-control', 'style':'width:100%'}),
            'street_address2': forms.TextInput(attrs={'class': 'form-control', 'style':'width:100%'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'style':'width:100%'})
        }

        labels = {
            'address_name': 'Address Name',
            'city': 'City',
            'street_address1': 'Address 1',
            'street_address2': 'Address 2',
        }
