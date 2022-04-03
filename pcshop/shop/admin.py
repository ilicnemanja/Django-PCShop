from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.subcategory import SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
                    'available', 'created', 'updated']
    list_filter = ['subcategory', 'available', 'online_shopping',
                   'in_stock', 'recommendation', 'latest']
    list_editable = ['price', 'available']
