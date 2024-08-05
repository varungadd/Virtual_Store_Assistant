import csv
from django.core.management.base import BaseCommand
from store_assistant.models import Product, ProductDescription

class Command(BaseCommand):
    help = 'Import product descriptions from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help=r'D:\CODER\Wallmart_Hackathon\virtual_store\product_description.csv')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['product_id']
                description = row['description']

                try:
                    product = Product.objects.get(product_id=product_id)
                    ProductDescription.objects.update_or_create(
                        product=product,
                        defaults={'description': description}
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported description for product ID {product_id}'))
                except Product.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Product with ID {product_id} does not exist'))
