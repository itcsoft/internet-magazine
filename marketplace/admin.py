from django.contrib import admin
from marketplace.models import Category2, Product, Order, OrderData

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

admin.site.register(Category2, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(OrderData)
admin.site.register(Order)