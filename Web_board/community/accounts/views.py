from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import AuthenticaationForm
from .models import User
from .forms import CustomUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):
    login_form = 