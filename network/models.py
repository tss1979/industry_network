from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название', **NULLABLE)
    model = models.CharField(max_length=255, verbose_name='модель', **NULLABLE)
    release_date = models.DateTimeField(default=timezone.now, verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} - {self.model}'


class Contact(models.Model):
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=255, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=255, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=255, verbose_name='улица', **NULLABLE)
    house = models.PositiveIntegerField(verbose_name='номер дома', **NULLABLE)


class LevelElement(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя', **NULLABLE)
    product = models.ManyToManyField(Product, verbose_name='продукт', related_name='products')
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакты')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, **NULLABLE)
    object_id = models.PositiveIntegerField(**NULLABLE)
    supplier = GenericForeignKey('content_type', 'object_id')
    credit = models.FloatField(verbose_name='задолжность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    def __str__(self):
        return f'{self.name}'


class Entrepreneur(LevelElement):
    pass


class Plant(LevelElement):
    pass


class Retail(LevelElement):
    pass
