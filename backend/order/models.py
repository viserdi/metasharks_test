import datetime

from django.db import models

from cars.models import CarColor, CarModel


class Order(models.Model):
    """Модель заказа автомобиля."""

    model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        verbose_name='Модель авто',
    )
    color = models.ForeignKey(
        CarColor,
        verbose_name='Цвет',
        on_delete=models.CASCADE,
    )
    count = models.PositiveSmallIntegerField(
        verbose_name='Количество',
    )
    date = models.DateField(
        verbose_name='Дата заказа',
        default=datetime.date.today
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id} авто {self.model} в количестве {self.count}'
