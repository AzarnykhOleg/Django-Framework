from django.core.management.base import BaseCommand
from marketplace.models import Product


class Command(BaseCommand):
    help = 'Добавление в БД нового продукта'

    def add_arguments(self, parser):
        parser.add_argument('-T', '--title', type=str, help='Префикс названия товара')
        parser.add_argument('-D', '--description', type=str, help='Префикс описания товара')
        parser.add_argument('-P', '--price', type=float, help='Префикс цены товара')
        parser.add_argument('-Q', '--quantity', type=int, help='Префикс количества товара')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']
        product = Product(title=title, description=description, price=price, quantity=quantity)
        product.save()
        self.stdout.write(f'{product}')
