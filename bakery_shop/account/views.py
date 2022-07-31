from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from . import models
from .services import utilities
from django.core.exceptions import ValidationError


@login_required
def account(request):
    return render(request, 'account/account.html')


class BakeryLogin(LoginView):
    template_name = 'account/login.html'


class BakeryLogout(LoginRequiredMixin, LogoutView):
    pass


def register_user(request):
    if request.method == 'POST':
        user_form = forms.RegisterUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            status, sms_code = utilities.send_activate_code(new_user.username)
            new_user.is_active = False
            new_user.is_activated = False
            new_user.sms_code_activated = sms_code
            new_user = user_form.save()
            return HttpResponseRedirect(f'activate/{new_user.username}')
        else:
            return render(request, 'account/register.html', {'user_form': user_form})
    else:
        user_form = forms.RegisterUserForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def activate_user(request, number_phone):
    if request.method == 'POST':
        code_form = forms.CodeFromUser(request.POST)
        code_from_user = code_form.data['user_code']
        new_user = models.BakeryUser.objects.get(username=number_phone)
        sms_code = new_user.sms_code_activated
        if code_from_user == sms_code:
            new_user.is_activated = True
            new_user.is_active = True
            new_user.save()
            return HttpResponseRedirect('/')
        else:
            code_form.add_error('user_code', 'Код не соответствует')
            return render(request, 'account/activate.html', {'code_form': code_form})

    else:
        code_form = forms.CodeFromUser()
    return render(request, 'account/activate.html', {'code_form': code_form})

