from django.core.management.base import BaseCommand
from models import Product
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        self.import_products()
        self.import_customer_behavior()

    def import_products(self):
        with open(r'D:\CODER\Wallmart_Hackathon\virtual_store\products_1.csv', 'r') as file:
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
