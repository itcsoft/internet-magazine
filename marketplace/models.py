from django.db import models


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
