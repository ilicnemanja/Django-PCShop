from django.db import models
from . import category


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(category.Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return f"[{self.category.name}] - {self.name}"
