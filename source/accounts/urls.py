from django.urls import path
from . import views
from .views import AccountCreateView

app_name = "accounts"

urlpatterns = [
    path("", views.login, name="login"),
    path("create", AccountCreateView.as_view(), name="create"),
]
