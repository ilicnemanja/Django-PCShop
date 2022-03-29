from django.contrib import admin
from .models.category import Category
from .models.product import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
                    'available', 'recommendation', 'latest', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'recommendation', 'latest']
    list_editable = ['price', 'available']