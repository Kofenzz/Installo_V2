from django import forms


class ProductSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search'}))
