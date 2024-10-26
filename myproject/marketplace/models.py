from decimal import Decimal

from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя клиента")
    email = models.EmailField(verbose_name="E-mail клиента")
    phone_number = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+?7?\d{9,12}$',
                message="Номер телефона должен быть введен в формате: '+79999999999'."
            )
        ],
        verbose_name="Телефон клиента"
    )
    address = models.TextField(verbose_name="Адрес клиента")
    date_of_registration = models.DateField(auto_now_add=True, verbose_name="Дата регистрации клиента")

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone_number: {self.phone_number}'


class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена продукта")
    quantity = models.IntegerField(verbose_name="Количество")
    date_of_addition = models.DateField(auto_now_add=True, verbose_name="Дата поставки")
    image = models.ImageField(upload_to='images/', default='1', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Product: {self.title}, описание: {self.description}, цена: {self.price}, количество: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    date_ordered = models.DateField(auto_now_add=False, verbose_name="Дата заказа")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Сумма заказа")

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ: {self.customer.name}, описание: {self.products}, сумма заказа: {self.total_price}'

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_price = total
        self.save()
