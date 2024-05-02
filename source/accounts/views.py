from django.shortcuts import render
from django.views.generic import CreateView
from .models import Account
from .forms import AccountForm


def login(req):
    return render(req, "")


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/account_form.html"
