from django.core.management.base import BaseCommand
from marketplace.models import Client


class Command(BaseCommand):
    help = 'Добавление в БД нового клиента'

    def add_arguments(self, parser):
        parser.add_argument('-N', '--name', type=str, help='Префикс имени клиента')
        parser.add_argument('-E', '--email', type=str, help='Префикс E-mail клиента')
        parser.add_argument('-P', '--phone', type=int, help='Префикс номера телефона клиента')
        parser.add_argument('-A', '--address', type=str, help='Префикс адреса клиента')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone']
        address = kwargs['address']
        client = Client(name=name, email=email, phone_number=phone_number, address=address)
        client.save()
        self.stdout.write(f'{client}')
