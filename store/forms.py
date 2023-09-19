from django import forms


class ProductSearchForm(forms.Form):
    name = forms.CharField(label='Product name', max_length=100, required=False)
