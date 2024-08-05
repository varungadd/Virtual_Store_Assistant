# store_assistant/models.py

from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    stock_availability = models.CharField(max_length=50)



    def __str__(self):
        return self.product_name


class CustomerBehavior(models.Model):
    customer_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ForeignKey relationship
    purchase_date = models.DateField()
    purchase_amount = models.FloatField()
    rating = models.IntegerField()
    review = models.TextField()
    search_queries = models.TextField()

    def __str__(self):
        return f"Customer {self.customer_id} - Product {self.product.product_name}"



class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.product.product_name} - {self.description[:50]}"
