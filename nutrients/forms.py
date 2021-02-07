"""
Django’s form functionality can simplify and automate
vast portions of this work, and can also do it more
securely than most programmers would be able to do
in code they wrote themselves.
"""


from django import forms

from nutrients.models import Unit, Nutrient


class NutrientForm(forms.ModelForm):
    """
    A form to process nutrients.
    """
    name = forms.CharField(max_length=200, required=True)
    unit = forms.ChoiceField(choices=Unit.choices, required=True)

    class Meta:
        """
        Form metadata.
        """
        model = Nutrient
        fields = ('name', 'unit')
