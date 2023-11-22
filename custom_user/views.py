from django.contrib import messages  # success message display on login page
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from custom_user.forms import UserForm, LoginForm, ProfileForm
from custom_user.models import User, Profile


class SignupView(CreateView):
    model = User
    form_class = UserForm

    success_url = reverse_lazy('login')
    template_name = 'custom_user/register.html'

    def form_valid(self, form):
        if form.is_valid():
            new_register = form.save(commit=False)
            new_register.first_name = new_register.first_name.title()
            new_register.last_name = new_register.last_name.title()
            new_register.email = new_register.email.lower()
            form.save()
            # succes message display on login page
            messages.success(self.request,
                             f"{new_register.first_name} {new_register.last_name}, your account has been registered.")
            return redirect('login')


class UserLoginPageView(SuccessMessageMixin, LoginView):
    template_name = 'custom_user/login.html'
    form_class = LoginForm


def logout(request):
    logouts(request)
    return redirect('homepage')


@login_required
def view_profile(request):
    user_profile = request.user.profile
    return render(request, 'custom_user/profile.html', {'user_profile': user_profile})


@login_required()
def edit_profile(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            # Update the Profile model with form data
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.first_name = user_profile.first_name.title()
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.last_name = user_profile.last_name.title()
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.address_1 = form.cleaned_data['address_1']
            user_profile.address_2 = form.cleaned_data['address_2']
            user_profile.user_type = form.cleaned_data['user_type']
            user_profile.save()

            return redirect('view_profile')

    else:
        # Initialize the form without instance argument
        form = ProfileForm(instance=user_profile)

    return render(request, 'custom_user/profile_menu/edit_profile.html', {'edit_profile': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'custom_user/profile_menu/profile_detail.html'
    model = Profile



