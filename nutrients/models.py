"""
Models related to Nutrients.
"""

from django.db import models
from datetime import datetime


class Unit(models.TextChoices):
    """
    Nutrient Unit.
    """
    GRAM = 'g', 'Gram'
    KILOGRAM = 'kg', 'Kilogram'
    CALORIE = 'cal', 'Calorie'
    KILOCALORIE = 'kcal', 'Kilocalorie'


class Nutrient(models.Model):
    """
    Nutrient Nutrient Entity.

    Attributes:
    ------------------------------
    id: Nutrient unique identifier.
    name: For example: Energetic Value, Proteins, Sugar, Fat, Carbohydrates.
    unit: For example: Kcal, g.
    created_at: Timestamp of the moment on which the Nutrient was added.
    updated_at: Timestamp of the last time the Nutrient was updated.
    """
    name = models.CharField(max_length=200, unique=True)
    unit = models.CharField(max_length=5,
                            choices=Unit.choices,
                            default=Unit.GRAM)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        """
        String Serializer
        """
        return f'{self.name} ({self.get_unit_display()})'

    def __repr__(self) -> str:
        """
        String Serializer
        """
        return f'<{self.__class__.__name__}: {self.name}>'

    class Meta:
        """
        Django Model Metadata.
        """
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Method responsible for catching save requests.
        """
        if not self.id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)
