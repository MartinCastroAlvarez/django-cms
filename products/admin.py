"""
The ModelAdmin class is the representation of a model in the admin interface.
"""
from django.contrib import admin

from products.models import Product, ProductNutrient


class ProductAdmin(admin.ModelAdmin):
    """
    Integration of the Product Model and the Django Admin.
    """


class ProductNutrientAdmin(admin.ModelAdmin):
    """
    Integration of the Product Nutrient Model and the Django Admin.
    """


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductNutrient, ProductNutrientAdmin)
