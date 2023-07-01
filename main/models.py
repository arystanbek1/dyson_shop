from django.db import models


class DysonModel(models.Model):
    name = models.CharField('Название Дайсона', max_length=40)
    image = models.ImageField()
    articul = models.CharField('Артикул', max_length=40)
    price = models.CharField('Цена', max_length=10)
    country = models.CharField('Страна', max_length=10)
    characteristic = models.TextField('Характеристика', max_length=200)
    color = models.CharField('Цвет', max_length=10)
    cap = models.CharField('Количество насадок', max_length=10)
    count = models.CharField('Количество в наличии', max_length=10)

    class Meta:
        verbose_name = 'Таблица Дайсонов'
        verbose_name_plural = 'Дайсон'

    def __str__(self):
        return self.name



