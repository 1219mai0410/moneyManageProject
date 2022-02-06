from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Logon(CreateView):
    form_class = LogonForm
    template_name = 'accounts/logon.html'
    success_url = reverse_lazy("accounts:login")

class Index(TemplateView):
    def get(self, request):
        params = {
            'user': request.user.username
        }
        return render(request, 'accounts/index.html', params)