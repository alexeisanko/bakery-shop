from django.shortcuts import render
from django.contrib.auth.views import LoginView


def account(request):
    return render(request, 'account/account.html')


class BakeryLogin(LoginView):
    template_name = 'account/login.html'

