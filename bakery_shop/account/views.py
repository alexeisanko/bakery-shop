from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def account(request):
    return render(request, 'account/account.html')


class BakeryLogin(LoginView):
    template_name = 'account/login.html'


class BakeryLogout(LoginRequiredMixin, LogoutView):
    pass



