from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView

from address.forms import AddressForm
from address.models import Address


# Create your views here.


@login_required()
def edit_address(request, address_id):
    address = Address.objects.get(pk=address_id)

    if request.method == 'POST':
        form = AddressForm(request.POST,instance=address)

        if form.is_valid():
            # Update the Address model with form data
            address.address_name = form.cleaned_data['address_name']
            address.address_name = address.address_name.title()
            address.recipient_name = form.cleaned_data['recipient_name']
            address.recipient_name = address.recipient_name.title()
            address.street_address1 = form.cleaned_data['street_address1']
            address.street_address1 = address.street_address1.lower()
            address.street_address2 = form.cleaned_data['street_address2']
            address.street_address2 = address.street_address2.lower()
            address.save()

            return redirect('address_list')

    else:
        # Initialize the form without instance argument
        form = AddressForm(instance=address)

    return render(request, 'custom_user/profile_menu/edit_address.html', {'edit_address': form})

class AddressListView(LoginRequiredMixin,ListView):
    model = Address
    template_name = 'custom_user/view_address.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Address.objects.filter(user=self.request.user)
        else:
            return Address.objects.none()