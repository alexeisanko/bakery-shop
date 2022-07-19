from django.db import models

# Create your models here.


class Products(models.Model):
    """Класс описывающий свойства блюд"""

    name = models.CharField(max_length=25, verbose_name='Наименование блюда')
    type_product = models.ForeignKey(
        'TypeProducts',
        on_delete=models.PROTECT,
        verbose_name='Тип блюда',
        to_field='type_product'
    )
    cost = models.FloatField(verbose_name='Цена за ед.')
    description = models.TextField(verbose_name='Описание блюда', blank=True)
    fats = models.IntegerField(verbose_name='Жиры', blank=True)
    protein = models.IntegerField(verbose_name='Белки', blank=True)
    carbohydrates = models.IntegerField(verbose_name='Углеводы', blank=True)
    image_product = models.ImageField(verbose_name='Изображение продукта', upload_to='products')


class TypeProducts(models.Model):
    """Свойства определенной категории блюд"""

    type_product = models.CharField(max_length=30, verbose_name='Тип блюда', unique=True)
    unit = models.CharField(max_length=15, verbose_name='Вид измерения')


class Shops(models.Model):
    """Описание магазинов"""

    name_shop = models.CharField(max_length=30, verbose_name="Название магазина")
    address_shop = models.CharField(max_length=100, verbose_name="Адрес магазина")


class CountProductsInShop(models.Model):
    """Хранит информацию о количество блюд в магазинах"""
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, to_field='name_shop', verbose_name='Магазин')
    product = models.ForeignKey(Shops, on_delete=models.CASCADE, to_field='name_shop', verbose_name='Блюдо')
    count = models.IntegerField(verbose_name='Количество')
