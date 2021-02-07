"""
The ModelAdmin class is the representation of a model in the admin interface.
"""
from django.contrib import admin

from nutrients.models import Nutrient


class NutrientAdmin(admin.ModelAdmin):
    """
    Integration of the Nutrient Model and the Django Admin.
    """


admin.site.register(Nutrient, NutrientAdmin)
