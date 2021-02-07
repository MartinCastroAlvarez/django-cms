"""
Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

import typing

from django.urls import path
from django.views.generic import TemplateView


urlpatterns: typing.List[path] = [
    # Displays the About Us HTML template.
    path('about',
         TemplateView.as_view(template_name="about.html"),
         name="malaga.about"),

    # Displays the Contact Us HTML template.
    path('contact',
         TemplateView.as_view(template_name="contact.html"),
         name="malaga.contact"),

    # Displays the Landing Page.
    path('',
         TemplateView.as_view(template_name="home.html"),
         name="malaga.home"),
]
