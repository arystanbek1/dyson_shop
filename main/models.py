from django.db import models
from .choices import get_status_choices


class DysonModel(models.Model):
    name = models.CharField('Название Дайсона', max_length=140)
    image = models.ImageField("Фото", null=True, blank=True)
    articul = models.CharField('Артикул', max_length=40)
    price = models.PositiveIntegerField('Цена')
    country = models.CharField('Страна', max_length=10)
    characteristic = models.TextField('Характеристика', max_length=200)
    color = models.CharField('Цвет', max_length=10)
    cap = models.PositiveIntegerField('Количество насадок')
    count = models.PositiveIntegerField('Количество в наличии')
    delete = models.BooleanField('Удалено', default=False)

    class Meta:
        verbose_name = 'Таблица Дайсонов'
        verbose_name_plural = 'Дайсон'

    def __str__(self):
        return self.name


class OrderDysonModel(models.Model):
    dyson_order = models.ForeignKey(DysonModel, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField('Заказаное количество')

    class Meta:
        verbose_name = 'Товары заказов'
        verbose_name_plural = 'Товар заказа'

    def __str__(self):
        return self.dyson_order.name


class OrderModel(models.Model):
    save_orders = models.ManyToManyField(OrderDysonModel)
    user = models.CharField('Имя клиента', max_length=255)
    mail = models.EmailField('Емэйл клента', max_length=255)
    phone = models.CharField('Номер клиента', max_length=11)
    finally_sum = models.PositiveIntegerField('Сумма заказа')
    status = models.CharField(choices=get_status_choices(), max_length=255)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return self.save_orders
