from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')
    image = models.ImageField(upload_to='images', verbose_name='Фото')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):  # перегрузка оператора
        return f'{self.pk} {self.title}'


class Person(models.Model):
    login = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class Hulk(models.Model):
    aaa = models.CharField(max_length=250)
