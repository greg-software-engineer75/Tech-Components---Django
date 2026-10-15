from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class Component(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Preço')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')