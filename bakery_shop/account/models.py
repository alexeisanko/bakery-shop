from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class BakeryUser(AbstractUser):
    """
    Класс для пользователей сайта. Дополнительно включает телефон и уровень лояльности
    """

    username = models.CharField(max_length=15, verbose_name="Номер телефона", unique=True)
    # phone_number_regex = RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$')
    # number_phone = models.CharField(validators=phone_number_regex, verbose_name="Номер телефона")
    id_loyalty = models.ForeignKey(
        'LoyaltyCard',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Уровень лояльности'
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class LoyaltyCard(models.Model):
    """Класс реализующий систему лояльности для покупателей"""

    level_loyalty = models.CharField(max_length=25, verbose_name="Уровень лояльности", unique=True)
    discount = models.IntegerField(verbose_name="Величина скидки")
    nex_level = models.CharField(max_length=25, blank=True, verbose_name="Следующий уровень лояльности")
    condition_to_next_level = models.IntegerField(blank=True, verbose_name="Необходимое условие для следующего уровня")

    def __str__(self):
        return self.level_loyalty

    class Meta:
        verbose_name = 'Система лояльности'
        verbose_name_plural = 'Система лояльности'


class Order(models.Model):
    """ Хранит себе все сделанные заказы пользователями"""

    numbers_order = models.IntegerField(verbose_name='Номер заказа')
    date_order = models.DateTimeField(verbose_name="Время заказа", auto_now_add=True)
    id_user = models.ForeignKey(BakeryUser, on_delete=models.CASCADE, verbose_name='id Покупателя')
    id_product = models.ForeignKey(
        'cooking.Products',
        on_delete=models.PROTECT,
        verbose_name='Наименование продукта',
    )
    count_product = models.IntegerField(verbose_name='Количество блюд')

    def __str__(self):
        return f'Заказ №{self.ordering} от {self.date_order}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class AddressUser(models.Model):
    """Модель для хранения адресов пользователя"""
    address = models.CharField(max_length=50, verbose_name='Адрес')
    id_user = models.ForeignKey(BakeryUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    id_shop = models.ForeignKey('cooking.Shops', on_delete=models.PROTECT, verbose_name='Магазин')

