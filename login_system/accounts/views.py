from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Account
from .forms import AccountForm
from django.core.exceptions import MultipleObjectsReturned


def home(req):
    return render(req, "core/home.html")


def login(request):
    return render(request, "")


class LoginView(TemplateView):
    template_name = "accounts/login.html"


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/account_form.html"
