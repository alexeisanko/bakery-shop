from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


@login_required
def account(request):
    return render(request, 'account/account.html')


class BakeryLogin(LoginView):
    template_name = 'account/login.html'


class BakeryLogout(LoginRequiredMixin, LogoutView):
    pass


class RegisterUser(CreateView):
    model = models.BakeryUser
    template_name = 'account/register.html'
    form_class = forms.RegisterUserForm
    success_url = '/'



