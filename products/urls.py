"""
Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

import typing

from django.urls import path
from django.contrib.auth.decorators import login_required

from products.views import product_list_view,\
                           product_details_view,\
                           product_nutrients_list_view,\
                           product_nutrient_details_view

urlpatterns: typing.List[path] = [
    # Endpoint for listing, searching and creating Products.
    path('',
         login_required(product_list_view),
         name="products.list"),

    # Endpoint for describing, updating and deleting a Product.
    path('<int:product_pk>/',
         login_required(product_details_view),
         name='products.details'),

    # Endpoint for listing, searching and creating Products Nutrients.
    path('<int:product_pk>/nutrients',
         login_required(product_nutrients_list_view),
         name='products.nutrients.list'),

    # Endpoint for describing, updating and deleting a Product.
    path('<int:product_pk>/nutrients/<int:nutrient_pk>',
         login_required(product_nutrient_details_view),
         name='products.nutrients.details'),
]
