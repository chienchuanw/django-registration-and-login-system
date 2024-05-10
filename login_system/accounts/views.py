from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Account
from .forms import AccountForm


def login(request):
    return render(request, "")

class LoginView(TemplateView):
    template_name = "accounts/login.html"




class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/account_form.html"
