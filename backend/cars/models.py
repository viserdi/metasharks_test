from django.db import models


class CarColor(models.Model):
    """Модель для справочника Цвет Машины."""
    name = models.CharField(
        verbose_name='Цвет машины',
        max_length=200,
        default=''
        )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Модель для справочника Марка Авто."""

    name = models.CharField(
        verbose_name='Марка авто',
        max_length=50,
        default='',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Модель для справочника Модель Авто."""

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='марка',
    )
    name = models.CharField(
        verbose_name='Модель авто',
        max_length=100,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name
