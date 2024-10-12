from django.core.management.base import BaseCommand
from marketplace.models import Client, Product, Order
import decimal


class Command(BaseCommand):
    help = 'Добавляет новый заказ в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('-C', '--client_id', type=str, help='Идентификатор клиента, оформляющего заказ')
        parser.add_argument('-P', '--product_ids', type=str, help='Список идентификаторов продуктов, разделенных запятыми')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        product_ids = kwargs['product_ids']

        # Найдем клиента по id
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором {client_id} не существует'))
            return

        # Разделим product_ids и найдем соответствующие продукты
        product_ids_list = product_ids.split(',')
        products = Product.objects.filter(id__in=product_ids_list)

        if not products:
            self.stdout.write(self.style.ERROR('Продукт не найден'))
            return

        if not product_ids_list or len(products) != len(product_ids_list):
            self.stdout.write(self.style.ERROR('Найдены не все продукты'))
            return

        # Создадим заказ
        total_price = sum(product.price * product.quantity for product in products)
        order = Order.objects.create(customer=client, total_price=total_price)
        order.products.set(products)
        order.save()
        self.stdout.write(self.style.SUCCESS(f'Успешно создан заказ с ID {order.id}'))
