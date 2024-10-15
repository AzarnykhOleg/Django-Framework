from datetime import datetime, date

from django.core.management.base import BaseCommand
from marketplace.models import Order, Client, Product
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Заполняет базу данных образцами заказов и связанными с ними данными'

    def handle(self, *args, **options):
        # Создаем несколько клиентов
        clients = [Client.objects.create(
            name=f'Client {i}',
            email=f'client{i}@example.com',
            phone_number=f'12345678{i}',
            address=f'Street {i}'
        ) for i in range(1, 6)]

        # Создаем несколько товаров
        products = [Product.objects.create(
            title=f'Product {i}',
            description=f'Description for Product {i}',
            price=Decimal(random.uniform(10, 100)),
            quantity=random.randint(1, 10),
        ) for i in range(1, 11)]

        # Создаем несколько заказов и связанных продуктов
        for i in range(1, 24):
            customer = random.choice(clients)
            products_in_order = random.sample(products, random.randint(1, 5))
            total_price = sum(product.price * product.quantity for product in products_in_order)
            set_date_year=random.randint(2023, 2024)
            set_date_month=random.randint(1, 12)
            set_date_day=random.randint(1, 28)
            order = Order.objects.create(
                customer=customer,
                total_price=total_price,
                date_ordered=date(set_date_year, set_date_month, set_date_day)
            )
            order.products.set(products_in_order)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))
