from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging

from django.utils import timezone

from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def home(request):
    logger.info('Home page accessed')
    return render(request, 'home.html')


def about(request):
    logger.info('About page accessed')
    context: dict[str, str] = {
        'title': 'Обо мне',
        'title_1': 'РАССКАЖУ',
        'title_2': 'НЕМНОГО',
        'title_3': 'О СЕБЕ',
    }
    return render(request, 'about.html', context)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'index.html')


def client_orders(request, client_id: int = None):
    logger.info('Client_orders page accessed')
    if client_id:
        client = get_object_or_404(Client, pk=client_id)
        order = Order.objects.filter(customer=client)
        today = timezone.now()

        # Заказы клиента за периоды времени
        order_week = order.filter(date_ordered__gte=today - timedelta(days=7))
        order_month = order.filter(date_ordered__gte=today - timedelta(days=30))
        order_year = order.filter(date_ordered__gte=today - timedelta(days=365))

        # Получаем уникальные продукты в заказах
        products_week = {product for order in order_week for product in order.products.all()}
        products_month = {product for order in order_month for product in order.products.all()}
        products_year = {product for order in order_year for product in order.products.all()}

        context: dict[str, str] = {
            'title': 'Заказы клиента',
            'title_1': 'ТОВАРЫ,',
            'title_2': 'ЗАКАЗАННЫЕ',
            'title_3': 'КЛИЕНТОМ',
            'title_4': client.name,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }

    else:
        context: dict[str, str] = {
            'title': 'Заказы клиента',
            'title_1': 'КЛИЕНТ',
            'title_2': 'НЕ',
            'title_3': 'НАЙДЕН',
        }
    return render(request, 'client_orders.html', context)

