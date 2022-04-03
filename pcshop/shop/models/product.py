from django.db import models
from . import subcategory


class Product(models.Model):
    subcategory = models.ForeignKey(
        subcategory.SubCategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products",
                              blank=True, default="nophoto.jpg")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    recommendation = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    online_shopping = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
