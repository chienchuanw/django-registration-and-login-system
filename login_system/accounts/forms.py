from django.forms import ModelForm
from .models import Account


class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields = ["username", "first_name", "last_name", "email", "password"]
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "password": "Password",
        }
