
from django.contrib.auth import logout as logouts
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages # succes message display on login page

from custom_user.forms import UserForm, LoginForm
from custom_user.models import User


class SignupView(CreateView):
    model = User
    form_class = UserForm

    success_url = reverse_lazy('login')
    template_name = 'custom_user/register.html'

    # success_message = "%(f_name)s (l_name)s ,your account has been registered."
    #
    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(cleaned_data, f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_register = form.save(commit=False)
            new_register.first_name = new_register.first_name.title()
            new_register.last_name = new_register.last_name.title()
            new_register.email = new_register.email.lower()
            form.save()
            messages.success(self.request,f"{new_register.first_name} {new_register.last_name}, your account has been registered.") # succes message display on login page
            return redirect('login')


class UserLoginPageView(SuccessMessageMixin, LoginView):
    template_name = 'custom_user/login.html'
    form_class = LoginForm


def logout(request):
    logouts(request)
    return redirect('homepage')
