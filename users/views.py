"""
A view function, or view for short, is a Python function that
takes a Web request and returns a Web response. This response
can be the HTML contents of a Web page, or a redirect, or a
404 error, or an XML document, or an image . . . or anything, really.
"""

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request: HttpRequest) -> HttpResponse:
    """
    Displays the login form and handles the login action.
    """
    redirect_to: str = request.POST.get('next', request.GET.get('next', '/'))
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return redirect(redirect_to)
    return render(request, "login.html", {
        'form': form,
        'next': redirect_to,
    })


def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Logs out the user and displays 'You are logged out' message.
    """
    logout(request)
    return render(request, "logout.html")


def signup_view(request: HttpRequest) -> HttpResponse:
    """
    Displays the signup form and handles the registration action.
    """
    redirect_to: str = request.POST.get('next', request.GET.get('next', '/'))
    form = UserCreationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user: User = authenticate(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(redirect_to)
    return render(request, "signup.html", {
        'form': form,
        'next': redirect_to,
    })
