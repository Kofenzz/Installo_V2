from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from custom_user.forms import UserForm, LoginForm
from custom_user.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as logouts


class SignupView(CreateView):
    model = User
    form_class = UserForm

    success_url = reverse_lazy('login')
    template_name = 'custom_user/register.html'

    # success_message = "{f_name} {l_name}"
    #
    # def get_success_message(self, cleaned_data):
    #     message = self.success_message + '. Your account has been registered.'
    #     return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_register = form.save(commit=False)
            new_register.first_name = new_register.first_name.title()
            new_register.last_name = new_register.last_name.title()
            new_register.email = new_register.email.lower()
            form.save()
            return redirect('login')


class UserLoginPageView(LoginView):
    template_name = 'custom_user/login.html'
    form_class = LoginForm


def logout(request):
    logouts(request)
    return redirect('homepage')

