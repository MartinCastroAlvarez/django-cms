"""
Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

import typing

from django.urls import path
from users.views import login_view, logout_view, signup_view

urlpatterns: typing.List[path] = [
    # Displays the login form and handles the login action.
    path('login', login_view, name='users.login'),

    # Logs out the user and displays 'You are logged out' message.
    path('signup', signup_view, name='users.signup'),

    # Displays the signup form and handles the registration action.
    path('logout', logout_view, name='users.logout'),
]
