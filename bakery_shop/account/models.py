from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class BakeryUser(AbstractUser):
    """
    Класс для пользователей сайта. Дополнительно включает телефон и уровень лояльности
    """

    username = None
    phone_number_regex = RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$')
    number_phone = models.CharField(validators=phone_number_regex, verbose_name="Номер телефона")
    id_loyalty = models.ForeignKey(
        'LoyaltyCard',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        to_field='level_loyalty'
    )

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователи'


class LoyaltyCard(models.Model):
    """Класс реализующий систему лояльности для покупателей"""

    level_loyalty = models.CharField(max_length=25, verbose_name="Уровень лояльности", unique=True)
    discount = models.IntegerField(verbose_name="Величина скидки")
    nex_level = models.CharField(max_length=25, blank=True, verbose_name="Следующий уровень лояльности")
    condition_to_next_level = models.IntegerField(blank=True, verbose_name="Необходимое условие для следующего уровня")

    class Meta:
        verbose_name = 'Система лояльноси'


class Order(models.Model):
    """ Хранит себе все сделанные заказы пользователями"""

    numbers_order = models.IntegerField(verbose_name='Номер заказа')
    date_order = models.DateTimeField(verbose_name="Время заказа", auto_now_add=True)
    id_user = models.ForeignKey(BakeryUser, on_delete=models.CASCADE, verbose_name='id Покупателя')

