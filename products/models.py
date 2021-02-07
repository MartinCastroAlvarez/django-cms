"""
Models related to Products.
"""

import enum
from datetime import datetime

from django.db import models

from nutrients.models import Nutrient


class Status(models.TextChoices):
    """
    Product Status Entity.
    """
    ACTIVE = 'a', 'Active'
    INACTIVE = 'i', 'Inactive'


class Product(models.Model):
    """
    Product Entity.

    Attributes:
    ------------------------------
    id: Product unique identifier.
    name: Name of the Product.
    description: Description of the Product.
    status: Either ACTIVE or INACTIVE.
    created_at: Timestamp of the moment on which the Product was added.
    updated_at: Timestamp of the last time the Product was updated.
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=5000)
    status = models.CharField(max_length=1,
                              choices=Status.choices,
                              default=Status.INACTIVE)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        """
        String Serializer
        """
        return self.name

    def __repr__(self) -> str:
        """
        String Serializer
        """
        return f'<{self.__class__.__name}: {self.name}>'

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


class ProductNutrient(models.Model):
    """
    Product Nutrient Entity.
    Each product can have multiple nutritional values.
    The product cannot have the same nutritional value multiple times.

    Attributes:
    ------------------------------
    id: Product Nutrient unique identifier.
    product: Foreign Key to the Product table.
    nutrient: Foreign Key to the Nutrient table.
    value: Nutrient Amount.
    created_at: Timestamp of the moment on which the Product Nutrient was added.
    updated_at: Timestamp of the last time the Product Nutrient was updated.
    """
    value = models.DecimalField(max_digits=10, decimal_places=2)
    nutrient = models.ForeignKey(Nutrient, related_name="products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="nutrients", on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        """
        String Serializer
        """
        return self.nutrient.name

    def __repr__(self) -> str:
        """
        String Serializer
        """
        return f'<{self.__class__.__name}: {self.productname} {self.nutrient.name}>'

    class Meta:
        """
        Django Model Metadata.
        """
        ordering = ['updated_at']
        constraints = [
            models.UniqueConstraint(fields=['product', 'nutrient'], name='product_nutrient')
        ]

    def save(self, *args, **kwargs):
        """
        Method responsible for catching save requests.
        """
        if not self.id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)
