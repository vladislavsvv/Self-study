from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True,
                              verbose_name='Почта')

    avatar = models.ImageField(upload_to='user/',
                               verbose_name='Аватар', **NULLABLE)

    phone = models.CharField(max_length=35,
                             verbose_name='Номер телефона', **NULLABLE)

    country = models.CharField(max_length=35,
                               verbose_name='Страна', **NULLABLE)

    is_active = models.BooleanField(default=True,
                                    verbose_name='Активность')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
