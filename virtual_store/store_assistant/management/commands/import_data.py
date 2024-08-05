from django.core.management.base import BaseCommand
from store_assistant.models import Product, CustomerBehavior, ProductDescription
from store_assistant.models import Product
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        self.import_products()
        self.import_customer_behavior()

    def import_products(self):
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Product.objects.update_or_create(
                    product_id=row['product_id'],
                    defaults={
                        'product_name': row['product_name'],
                        'category': row['category'],
                        'price': row['price'],
                        'location': row['location'],
                        'stock_availability': row['stock_availability']
                    }
                )
        pass
    
    def import_customer_behavior(self):
        with open(r'D:\CODER\Wallmart_Hackathon\virtual_store\customer_behavior.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert date format
                try:
                    purchase_date = datetime.strptime(row['purchase_date'], '%d-%m-%Y').strftime('%Y-%m-%d')
                except ValueError:
                    self.stderr.write(f"Invalid date format for {row['purchase_date']}")
                    continue
                
                CustomerBehavior.objects.update_or_create(
                    customer_id=row['customer_id'],
                    purchase_date=purchase_date,
                    defaults={
                        'purchase_amount': row['purchase_amount'],
                        'rating': row['rating'],
                        'review': row['review'],
                        'search_queries': row['search_queries'],
                        'product_id': row['product_id']
                    }
                )
        pass
    
    def import_product_descriptions(self):
        with open(r'D:\CODER\Wallmart_Hackathon\virtual_store\product_description.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['product_id']
                product_name = row['product_name']
                description = row['description']
                
                # Get or create the product
                product, created = Product.objects.get_or_create(
                    product_id=product_id,
                    defaults={'product_name': product_name}
                )
                
                # Update or create product description
                ProductDescription.objects.update_or_create(
                    product=product,
                    defaults={'description': description}
                )
        