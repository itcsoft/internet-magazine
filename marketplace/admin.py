from django.contrib import admin
from marketplace.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
