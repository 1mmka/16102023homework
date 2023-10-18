from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
class Register(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home_page')
    template_name = 'register.html'
    success_message = 'Successfully registered!'

    



