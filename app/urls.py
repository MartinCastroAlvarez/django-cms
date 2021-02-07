"""
App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

import typing

from django.contrib import admin
from django.urls import path, include

urlpatterns: typing.List[path] = [
    # Django Admin.
    path('admin/', admin.site.urls),

    # Views for managing Products, ingredients, nutritional values, etc.
    path('products/', include('products.urls'), name='products'),

    # Views for managing Nutrients.
    path('nutrients/', include('nutrients.urls'), name='nutrients'),

    # Views responsible for User Authentication and Profile editing.
    path('users/', include('users.urls'), name='users'),

    # Structural views such as the Landing Page or the Contact Us Page.
    path('', include('malaga.urls'), name='malaga'),
]
