"""
Модуль: Модель пользователя
Этот модуль содержит модель пользователя для приложения.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


NULLABLE = {
    'null': True,
    'blank': True,
}


class User(AbstractUser):
    """
    Пользовательская модель с дополнительными полями и разрешениями.

    Атрибуты:
        email (EmailField): Уникальный адрес электронной почты пользователя.
        phone (CharField): Номер телефона пользователя. Допускает пустое значение.
        avatar (ImageField): Изображение аватара пользователя. Допускает пустое значение.
        verification_code (CharField): Проверочный код пользователя. Допускает пустое значение.
        is_superuser (BooleanField): Указывает, является ли пользователь суперпользователем.
        is_staff (BooleanField): Указывает, является ли пользователь сотрудником.
        is_active (BooleanField): Указывает, активен ли аккаунт пользователя.

    Meta:
        verbose_name (str): Единственное имя для модели.
        verbose_name_plural (str): Множественное имя для модели.
        ordering (tuple): Порядок сортировки по умолчанию для запросов.
        permissions (list): Список разрешений для модели.
    """
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='почта')

    phone = models.CharField(
        max_length=50,
        verbose_name='номер телефона',
        **NULLABLE)
    avatar = models.ImageField(
        upload_to='users/',
        verbose_name='аватар',
        **NULLABLE)
    verification_code = models.CharField(
        max_length=25,
        verbose_name='проверочный код',
        **NULLABLE)

    is_superuser = models.BooleanField(
        default=False,
        verbose_name='администратор сервиса')
    is_staff = models.BooleanField(
        default=False,
        verbose_name='сотрудник сервиса')
    is_active = models.BooleanField(
        default=False,
        verbose_name='метка активности')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)

        permissions = [
            ('set_is_activated', 'переключатель метки активности')
        ]
