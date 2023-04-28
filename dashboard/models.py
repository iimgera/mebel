from django.db import models
from markets.models import Location, Product


class Customer(models.Model):
    name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
        )
    age = models.IntegerField(
        blank=True, 
        null=True, 
        verbose_name='Возраст'
        )
    gender = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name='Гендер'
        )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, 
        related_name='location',
        verbose_name='Местоположение'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'




class Employee(models.Model):
    name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
        )
    age = models.IntegerField(
        blank=True, 
        null=True, 
        verbose_name='Возраст'
        )
    gender = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name='Гендер'
        )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, 
        # related_name='location',
        verbose_name='Местоположение'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    

class Order(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='product', 
        verbose_name='Продукт'
        )
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        related_name='employee', 
        verbose_name='Сотрудник'
        )
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='customer', 
        verbose_name='Клиент'
        )
    order_date = models.DateTimeField( 
        verbose_name='Дата заказа'
        )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    
