from django.urls import path
from . import views
from .views import AccountCreateView, LoginView

app_name = "accounts"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("create/", AccountCreateView.as_view(), name="create"),
]
