from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from adress.forms import AddressForm
from adress.models import Address


# Create your views here.


@login_required()
def edit_address(request, pk):
    address = Address.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)

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

            return redirect('view_address')

    else:
        # Initialize the form without instance argument
        form = AddressForm(instance=address)

    return render(request, 'custom_user/profile_menu/edit_address.html', {'edit_address': form})


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'custom_user/view_address.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Address.objects.filter(user=self.request.user)
        else:
            return Address.objects.none()


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'custom_user/profile_menu/create_address.html'
    success_url = reverse_lazy('view_address')

    # fields = ['address_name', 'recipient_name', 'street_address1','street_address2', 'city', 'postal_code']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Address has been created successfully.')

        return super().form_valid(form)


class AddressDeleteView(LoginRequiredMixin,DeleteView):
    model = Address
    success_url = reverse_lazy('view_address')
    template_name = 'custom_user/profile_menu/delete_address.html'
    context_object_name = 'delete_address'