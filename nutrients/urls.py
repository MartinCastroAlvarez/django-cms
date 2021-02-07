"""
Nutrient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

import typing

from django.urls import path
from django.contrib.auth.decorators import login_required

from nutrients.views import nutrient_list_view, nutrient_details_view

urlpatterns: typing.List[path] = [
    # Endpoint for listing, searching and creating Nutrients.
    path('',
         login_required(nutrient_list_view),
         name="nutrients.list"),

    # Endpoint for describing, updating and deleting a Nutrient.
    path('<int:nutrient_pk>/',
         login_required(nutrient_details_view),
         name='nutrients.details'),
]
