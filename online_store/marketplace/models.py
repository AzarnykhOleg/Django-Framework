from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+?7?\d{9,12}$',
                message="Номер телефона должен быть введен в формате: '+79999999999'."
            )
        ]
    )
    # phone_number = models.IntegerField()
    address = models.TextField()
    date_of_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone_number: {self.phone_number}'


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_of_addition = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.title}, описание: {self.description}, цена: {self.price}, количество: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
