from pyexpat import model
from django.db import models
from django.forms import model_to_dict


class Category2(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    img = models.ImageField("Изображение", upload_to='upload/categories')


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    price = models.IntegerField("Цена", default=0)
    category = models.ForeignKey(Category2, verbose_name="Категория", on_delete=models.CASCADE)
    description = models.CharField("Описание", max_length=255, default='', blank=True, null=True)
    image = models.ImageField("Изображение", upload_to='upload/products')


class OrderData(models.Model):
    name = models.CharField('ФИО', max_length=255)
    number = models.CharField('Номер Телефона', max_length=255)
    email = models.EmailField('Email')
    address = models.CharField('Адрес', max_length=255)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField('Товар', max_length=255)
    price = models.IntegerField('Цена')
    count = models.IntegerField('Количество')
    total_sum = models.IntegerField('Общая сумма')
    customer = models.ForeignKey(OrderData, on_delete=models.CASCADE, verbose_name='Получатель')
    sent_at = models.DateTimeField('Время отправки', auto_now_add=True)
