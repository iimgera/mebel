from django.db import models





class Location(models.Model):
    country = models.CharField(
        max_length=20, 
        blank=True, 
        null=True,
        verbose_name='Страна'
        ) 

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

        


class Product(models.Model):
    title = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name='Название'
        )
    description = models.TextField(
        null=True,
        verbose_name='Описание'
        )
    price = models.DecimalField(
        max_digits=20, 
        decimal_places=0, 
        null=True,
        verbose_name='Цена'
        )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'