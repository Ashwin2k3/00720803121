# products/models.py

from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.FloatField()
    company = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.name
