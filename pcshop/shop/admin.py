from django.contrib import admin
from .models.category import Category
from .models.product import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
                    'available', 'created', 'updated']
    list_filter = ['category', 'available', 'online_shopping',
                   'in_stock', 'recommendation', 'latest']
    list_editable = ['price', 'available']
