from django.http import HttpResponse
from django.shortcuts import render

from users.forms import LoginForm


def login_user(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    return HttpResponse("logout")