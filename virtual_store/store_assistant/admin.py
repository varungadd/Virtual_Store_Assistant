from django.contrib import admin
from .models import Product, CustomerBehavior, ProductDescription

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'category', 'price', 'location', 'stock_availability')
    search_fields = ('product_name', 'category')
    list_filter = ('category',)

@admin.register(CustomerBehavior)
class CustomerBehaviorAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'purchase_date', 'purchase_amount', 'rating', 'product')
    search_fields = ('customer_id', 'review', 'search_queries')
    list_filter = ('purchase_date', 'rating', 'product')

@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'description')
    search_fields = ('product', 'product_name', 'description')
    list_filter = ('product',)
