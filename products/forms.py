"""
Django’s form functionality can simplify and automate
vast portions of this work, and can also do it more
securely than most programmers would be able to do
in code they wrote themselves.
"""


from django import forms

from products.models import Status, Product, ProductNutrient
from nutrients.models import Nutrient


class ProductForm(forms.ModelForm):
    """
    A form to process Products.
    """
    name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, max_length=5000, required=True)
    status = forms.ChoiceField(choices=Status.choices, required=True)

    class Meta:
        """
        Form metadata.
        """
        model = Product
        fields = ('name', 'description', 'status')


class ProductNutrientForm(forms.ModelForm):
    """
    A form to process Products Nutrients.
    """
    value = forms.DecimalField(min_value=0, required=True)
    nutrient = forms.ModelChoiceField(Nutrient.objects, required=True)
    product = forms.ModelChoiceField(Product.objects, required=True)

    class Meta:
        """
        Form metadata.
        """
        model = ProductNutrient
        fields = ('value', 'nutrient', 'product')
